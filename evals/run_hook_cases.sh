#!/bin/sh
# Feeds each test case to a hook script as Claude Code would (JSON on stdin) and compares exit codes.
# Usage: sh run.sh <hook-script> <cases.tsv>
# cases.tsv: expected_exit<TAB>tool_name<TAB>command[<TAB>description]
#   Lines starting with # are skipped. The token <NL> in a command becomes a real newline.
PATH="/usr/bin:/bin:$PATH"
export PATH

HOOK="$1"
CASES="$2"
tab="$(printf '\t')"
n=0
bad=0
while IFS="$tab" read -r expected tool cmd desc || [ -n "$expected" ]; do
  case "$expected" in ''|\#*) continue ;; esac
  [ -n "$desc" ] || desc="test"
  esc="$(printf '%s' "$cmd" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' -e 's/<NL>/\\n/g')"
  desc_esc="$(printf '%s' "$desc" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"
  payload="$(printf '{"session_id":"t","cwd":"C:\\\\Users\\\\Usuario\\\\Documents\\\\Projects\\\\mazos_magic","hook_event_name":"PreToolUse","tool_name":"%s","tool_input":{"command":"%s","description":"%s"}}' "$tool" "$esc" "$desc_esc")"
  printf '%s' "$payload" | sh "$HOOK" >/dev/null 2>&1
  got=$?
  n=$((n + 1))
  if [ "$got" = "$expected" ]; then
    echo "ok   $got [$tool] $cmd"
  else
    bad=$((bad + 1))
    echo "FAIL expected=$expected got=$got [$tool] $cmd"
  fi
done < "$CASES"
echo "cases=$n failures=$bad"
