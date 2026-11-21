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
FABLE_TOKEN_FILE="${TMPDIR:-/tmp}/agent-model-cases-no-fable-$$"  # never the real authorization file
export FABLE_TOKEN_FILE
OPUS_MAX_TOKEN_FILE="${TMPDIR:-/tmp}/agent-model-cases-no-opus-max-$$"  # never the real file
export OPUS_MAX_TOKEN_FILE
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
# Fable 5.2 (owner, 2026-11-14; no expiry since 2026-11-15): allowed only with his authorization file, at its effort.
FABLE_TOKEN_FILE="${TMPDIR:-/tmp}/agent-model-cases-fable-$$"
export FABLE_TOKEN_FILE
fable_case() {  # expected, effort, token content ("-" = no file), age in minutes
  rm -f "$FABLE_TOKEN_FILE"
  if [ "$3" != "-" ]; then
    printf '%s\n' "$3" > "$FABLE_TOKEN_FILE"
    [ "$4" = 0 ] || touch -d "$4 minutes ago" "$FABLE_TOKEN_FILE"
  fi
  printf '{"tool_name":"Agent","tool_input":{"description":"t","prompt":"t","subagent_type":"deck-builder","model":"fable","effort":"%s"}}' "$2" | sh "$HOOK" >/dev/null 2>&1
  got=$?
  n=$((n + 1))
  if [ "$got" = "$1" ]; then echo "ok   $got fable effort=$2 token=$3 age=$4"; else bad=$((bad + 1)); echo "FAIL expected $1 got $got fable effort=$2 token=$3 age=$4"; fi
}
fable_case 2 high - 0
fable_case 0 high "2026-11-14T22:00:00Z high" 0
fable_case 2 max "2026-11-14T22:00:00Z high" 0
fable_case 0 max "2026-11-14T22:00:00Z max" 30
fable_case 0 high "2026-11-14T22:00:00Z high" 1500  # an old authorization still holds (no expiry)
rm -f "$FABLE_TOKEN_FILE"
# Opus 5.5 max (owner, 2026-11-21): one call per authorization, within 30 minutes.
OPUS_MAX_TOKEN_FILE="${TMPDIR:-/tmp}/agent-model-cases-opus-max-$$"
export OPUS_MAX_TOKEN_FILE
max_case() {  # expected, effort, token ("-" none, "new", or an age in minutes), label
  if [ "$3" = "-" ]; then rm -f "$OPUS_MAX_TOKEN_FILE"; elif [ "$3" != "keep" ]; then
    date -u > "$OPUS_MAX_TOKEN_FILE"; [ "$3" = new ] || touch -d "$3 minutes ago" "$OPUS_MAX_TOKEN_FILE"; fi
  printf '{"tool_name":"Agent","tool_input":{"description":"t","prompt":"t","subagent_type":"deck-builder","model":"opus","effort":"%s"}}' "$2" | sh "$HOOK" >/dev/null 2>&1
  got=$?
  n=$((n + 1))
  if [ "$got" = "$1" ]; then echo "ok   $got opus effort=$2 token=$3 $4"; else bad=$((bad + 1)); echo "FAIL expected $1 got $got opus effort=$2 token=$3 $4"; fi
}
max_case 2 max - "no authorization"
max_case 0 max new "fresh authorization"
max_case 2 max keep "used up by the previous call"
max_case 2 max 45 "older than 30 minutes"
max_case 0 high 45 "opus high never needs it"
max_case 2 xhigh new "xhigh stays blocked"
rm -f "$OPUS_MAX_TOKEN_FILE"
echo "$n cases, $bad failures"
[ "$bad" = 0 ]
