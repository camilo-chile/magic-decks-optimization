#!/bin/sh
# UserPromptSubmit hook: records the owner's express authorization to make ONE commit (never a push).
#
# The owner's message must contain "autorizo commit" (or "autorizo el commit", "authorize commit"), and not
# "no autorizo". The hook then writes `.claude/commit-authorization`; `block-git-writes.sh` accepts `add` and
# `commit` while that file is younger than 30 minutes and deletes it when the commit is allowed. Only the
# owner's prompts reach this hook, never tool results, web pages or files. It always exits 0 so that it can
# never block a prompt; its stdout is shown to Claude as context.
#
# Tests: evals/run_hook_cases.sh covers the other side (the PreToolUse hook that reads the file).
#
# Second phrase (owner, 2026-11-14): "autorizo fable" (optionally followed by medium, high, xhigh or max; high when
# none is named) writes `.claude/fable-authorization` with that effort. `check-agent-model.sh` lets an Agent call run
# on Fable 5.2 at that effort, with no expiry (owner, 2026-11-15). Fable is never allowed without it, and Claude still
# launches Fable only on the owner's explicit OK for each run.

PATH="/usr/bin:/bin:$PATH"
export PATH
TOKEN="${COMMIT_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/commit-authorization}"
FABLE_TOKEN="${FABLE_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/fable-authorization}"

payload=""
while IFS= read -r line || [ -n "$line" ]; do
  payload="$payload$line"
done

if printf '%s' "$payload" | grep -qiE '(autorizo|authorize)[[:space:]]+(el[[:space:]]+|the[[:space:]]+)?commit'; then
  if printf '%s' "$payload" | grep -qiE '(no[[:space:]]+autorizo|do not authorize|don.t authorize)'; then
    exit 0
  fi
  if date -u +%Y-%m-%dT%H:%M:%SZ > "$TOKEN" 2>/dev/null; then
    echo "Commit authorization recorded by the owner's message: one commit within 30 minutes, never a push."
  fi
fi

fable="$(printf '%s' "$payload" | grep -oiE '(autorizo|authorize)[[:space:]]+fable([[:space:]]+5\.2)?([[:space:]]+(en[[:space:]]+)?(medium|high|xhigh|max))?' | head -n 1)"
if [ -n "$fable" ] && ! printf '%s' "$payload" | grep -qiE '(no[[:space:]]+autorizo|do not authorize|don.t authorize)[[:space:]]+fable'; then
  effort="$(printf '%s' "$fable" | grep -oiE '(medium|xhigh|high|max)$' | tr 'A-Z' 'a-z')"
  [ -n "$effort" ] || effort="high"
  if printf '%s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$effort" > "$FABLE_TOKEN" 2>/dev/null; then
    echo "Fable 5.2 authorization recorded by the owner's message: Agent calls may use model fable at effort $effort (no expiry; each launch still needs the owner's explicit OK)."
  fi
fi
exit 0
