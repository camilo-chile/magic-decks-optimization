#!/bin/sh
# PreToolUse hook (Bash, PowerShell and Monitor): git is read-only for Claude, with one exception.
#
# Exception (owner decision, 2026-10-19): `add` and `commit` are allowed only while the owner's express
# authorization is on record, a one-shot file `.claude/commit-authorization` that the UserPromptSubmit hook
# (`authorize-commit.sh`) writes when the owner's message says "autorizo commit". It expires after 30
# minutes and is used up by the commit. Even then: no `push`, `--amend`, `--no-verify`, `-a`, `--allow-empty`,
# no author or date overrides, no GIT_* variables, no interactive forms; a message (`-m` or `-F`) is required.
# Claude cannot write the file through a command (any command that names it is blocked here) nor through the
# Write and Edit tools (permission deny rules).
#
# Allowlist: every git invocation in the command must use a read-only subcommand
# (status, diff, log, show, ls-files, check-ignore, check-attr, var, rev-parse, blame,
# grep, shortlog, describe, cat-file, ls-tree, help, version, plus read-only forms of
# config, branch and remote). Anything else, including aliases, unknown global options
# and calls whose subcommand cannot be read (git kept in a variable, argument arrays),
# is blocked. Exit code 2 blocks the call and sends stderr back to Claude.
#
# Scope: this stops natural mistakes, including quoted full paths such as
# "C:\Program Files\Git\cmd\git.exe" commit. It cannot read inside script files, renamed
# binaries or subprocesses (for example a script written first and run later); permission
# rules must not allow those, and the user's review of every diff remains the main control.
#
# Robustness: on Windows the PATH can list a WSL directory first, whose binaries fail with
# "Exec format error". So this script reads stdin with shell builtins, puts the Git for
# Windows tools first, and fails closed (blocks) whenever it cannot evaluate a command.
#
# Tests: evals/hook_cases.tsv holds the command table this script was checked against.

PATH="/usr/bin:/bin:$PATH"
export PATH
set -f

# COMMIT_TOKEN_FILE exists only so that evals/run_hook_cases.sh can test the exception.
TOKEN="${COMMIT_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/commit-authorization}"
TOKEN_MINUTES=30

block() {
  echo "Blocked by project rule: git is read-only for Claude ($1). Propose the command to the user instead." >&2
  exit 2
}

payload=""
while IFS= read -r line || [ -n "$line" ]; do
  payload="$payload$line"
done

# No fast path on the raw text: quotes can split the word (g''it), so every command is
# normalized first. The tools must work before we trust their output.
[ "$(printf 'x' | sed 's/x/y/' 2>/dev/null)" = "y" ] || block "hook self-test failed: sed"

# 1. Take tool_input.command (a JSON string). If it cannot be found, scan the whole payload.
cmd="$(sed -n 's/.*"command":"\(\([^"\\]\|\\.\)*\)".*/\1/p' <<EOF
$payload
EOF
)" || block "hook could not parse the payload"
[ -n "$cmd" ] || cmd="$payload"
case "$cmd" in
  *commit-authorization*) block "the commit authorization file is written only by the UserPromptSubmit hook" ;;
esac

# 2. Normalize: unescape JSON, turn backslashes into slashes (Windows paths), delete quotes
#    and backticks (so "git.exe" commit and g''it are seen), cut at shell separators, and
#    start every git token on its own line. A sentinel marks the real end of the command.
lines="$(sed -e 's/\\\\\\"//g' \
             -e "s/\\\\\\\\'//g" \
             -e 's/\\\\/\x01/g' \
             -e 's/\\[nr]/;/g' \
             -e 's/\\t/ /g' \
             -e 's/\\"//g' \
             -e 's/\\\//\//g' \
             -e 's/\x01/\//g' \
             -e "s/[\"'\`]//g" \
             -e 's/$/ __HOOK_END__/' \
             -e 's/[;|&(){}<>,]/\n/g' <<EOF
$cmd
EOF
)" || block "hook could not normalize the command"
lines="$(sed -E 's/(^|[^[:alnum:]_.-])([Gg][Ii][Tt](-[[:alnum:]-]+)?(\.[Ee][Xx][Ee])?)([[:space:]]|$)/\1\n\2\5/g' <<EOF
$lines
EOF
)" || block "hook could not split the command"

# 3. Check each git invocation.
authorized() {
  [ -f "$TOKEN" ] || return 1
  [ -n "$(find "$TOKEN" -mmin "-$TOKEN_MINUTES" 2>/dev/null)" ]
}

# The raw command must not hide a forbidden flag behind a separator inside a commit message.
check_raw_write() {
  case "$cmd" in
    *GIT_*) block "GIT_* variable together with $1" ;;
    *--amend*|*--no-verify*|*--allow-empty*|*--force*|*--author*|*--date*|*--reset-author*|*--gpg-sign*|*--no-gpg-sign*) block "forbidden option together with $1" ;;
  esac
}

check_args() {
  # Read-only subcommands must not write files or start other programs.
  for a in "$@"; do
    case "$a" in
      --output*|-O*|--open-files-in-pager*|--ext-diff) block "option $a" ;;
    esac
  done
}

check_line() {
  final=0
  case "$1" in *__HOOK_END__*) final=1 ;; esac
  set -- ${1%%__HOOK_END__*}
  tok="$1"
  shift
  sub=""
  case "$tok" in
    [Gg][Ii][Tt]-*)
      sub="${tok#???-}"
      sub="${sub%.[Ee][Xx][Ee]}"
      ;;
  esac
  if [ -z "$sub" ]; then
    while [ $# -gt 0 ]; do
      case "$1" in
        -C) shift; [ $# -gt 0 ] && shift ;;
        --no-pager|-P|--no-optional-locks) shift ;;
        --version|--help|-h) return 0 ;;
        -*) block "global option $1" ;;
        *) break ;;
      esac
    done
    if [ $# -eq 0 ]; then
      # A bare git token is fine only at the very end (e.g. "where.exe git"); before a
      # separator it may be a variable call such as $g = "...git.exe"; & $g commit.
      [ "$final" -eq 1 ] && return 0
      block "git call whose subcommand cannot be read"
    fi
    sub="$1"
    shift
  fi
  case "$sub" in
    status|diff|log|show|ls-files|check-ignore|check-attr|var|rev-parse|blame|grep|shortlog|describe|cat-file|ls-tree|help|version)
      check_args "$@"
      ;;
    add)
      authorized || block "add needs the owner's express authorization (a message with 'autorizo commit')"
      check_raw_write add
      for a in "$@"; do
        case "$a" in
          -A|--all|-u|--update|-v|--verbose|--) ;;
          -*) block "add option $a" ;;
        esac
      done
      ;;
    commit)
      authorized || block "commit needs the owner's express authorization (a message with 'autorizo commit')"
      check_raw_write commit
      has_msg=0
      for a in "$@"; do
        case "$a" in
          -m|-F|--message|--file|--message=*|--file=*) has_msg=1 ;;
          -[a-zA-Z]*|--[a-zA-Z]*) block "commit option $a" ;;
        esac
      done
      [ "$has_msg" -eq 1 ] || block "commit without a message (-m or -F) would open an editor"
      rm -f "$TOKEN"
      ;;
    config)
      read_form=0
      for a in "$@"; do
        case "$a" in
          set|unset|edit|rename-section|remove-section|--add|--unset|--unset-all|--replace-all|--rename-section|--remove-section|-e|--edit)
            block "config write" ;;
          get|list|--get|--get-all|--get-regexp|--get-urlmatch|--list|-l) read_form=1 ;;
        esac
      done
      [ "$read_form" -eq 1 ] || block "config without an explicit read form (--get, --list)"
      ;;
    branch)
      for a in "$@"; do
        case "$a" in
          -a|-r|-v|-vv|--all|--remotes|--verbose|--list|--show-current|--no-color|--color|--sort=*|--format=*) ;;
          *) block "branch $a" ;;
        esac
      done
      ;;
    remote)
      case "${1:-}" in
        ''|-v|--verbose|get-url|show) ;;
        *) block "remote $1" ;;
      esac
      ;;
    *)
      block "subcommand $sub"
      ;;
  esac
  return 0
}

printf '%s\n' "$lines" | {
  while IFS= read -r l || [ -n "$l" ]; do
    case "$l" in
      [Gg][Ii][Tt]|[Gg][Ii][Tt][[:space:]]*|[Gg][Ii][Tt].[Ee][Xx][Ee]|[Gg][Ii][Tt].[Ee][Xx][Ee][[:space:]]*|[Gg][Ii][Tt]-*)
        check_line "$l"
        ;;
    esac
  done
  exit 0
}
exit $?
