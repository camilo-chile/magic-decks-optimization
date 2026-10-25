#!/bin/sh
# Feeds each test case to the model-policy hook as Claude Code would (JSON on stdin) and compares exit codes.
# Usage: sh evals/run_agent_model_cases.sh <hook-script> <cases.tsv>
# cases.tsv: expected_exit<TAB>model<TAB>effort<TAB>subagent_type<TAB>prompt
#   "-" means the field is not sent. Lines starting with # are skipped. The prompt is escaped like real JSON,
#   so a prompt that mentions "model":"opus" must not change the verdict.
#   The project agents come from this repository; the user agent folder is replaced by an empty one.
PATH="/usr/bin:/bin:$PATH"
export PATH

HOOK="$1"
CASES="$2"
tab="$(printf '\t')"
here="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE_PROJECT_DIR="$here"
CLAUDE_USER_DIR="${TMPDIR:-/tmp}/agent-model-cases-empty-$$"
export CLAUDE_PROJECT_DIR CLAUDE_USER_DIR
n=0
bad=0
while IFS="$tab" read -r expected model effort stype prompt || [ -n "$expected" ]; do
  case "$expected" in
    ''|\#*) continue ;;
  esac
  [ -n "$prompt" ] && [ "$prompt" != "-" ] || prompt="test"
  esc="$(printf '%s' "$prompt" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g')"
  extra=""
  [ "$stype" = "-" ] || extra="$extra,\"subagent_type\":\"$stype\""
  [ "$model" = "-" ] || extra="$extra,\"model\":\"$model\""
  [ "$effort" = "-" ] || extra="$extra,\"effort\":\"$effort\""
  payload="$(printf '{"session_id":"t","hook_event_name":"PreToolUse","tool_name":"Agent","tool_input":{"description":"t","prompt":"%s"%s}}' "$esc" "$extra")"
  printf '%s' "$payload" | sh "$HOOK" >/dev/null 2>&1
  got=$?
  n=$((n + 1))
  if [ "$got" = "$expected" ]; then
    echo "ok   $got [$stype] model=$model effort=$effort"
  else
    bad=$((bad + 1))
    echo "FAIL expected $expected got $got [$stype] model=$model effort=$effort :: $prompt"
  fi
done < "$CASES"
echo "$n cases, $bad failures"
[ "$bad" = 0 ]
