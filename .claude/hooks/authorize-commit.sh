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

PATH="/usr/bin:/bin:$PATH"
export PATH
TOKEN="${COMMIT_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/commit-authorization}"

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
exit 0
