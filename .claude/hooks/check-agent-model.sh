#!/bin/sh
# PreToolUse hook (Agent): the model policy (owner decisions 2026-10-25 and 2026-11-07).
#
# Only three model + effort pairs are allowed on an Agent call:
#   opus + high      the hardest, most delicate or "we cannot fail" work
#   opus + medium    planning, orchestration, general chat, code (medium work)
#   haiku + xhigh    repetitive and light work
# plus one special pair for driving the browser (owner, 2026-11-07, on trial): haiku + medium, only for the
# browser agents listed in BROWSER_AGENTS.
# Anything else is blocked (exit code 2 sends the message back to Claude): Opus xhigh, max or low, Sonnet,
# Haiku at another level, Fable, other model versions, a model without its effort, or an effort without a model.
#
# A call that sets neither model nor effort is allowed only when
#   - it is a `fork` (inherits the session, which settings.json pins to Opus medium), or
#   - its subagent_type names a definition (`.claude/agents/<name>.md` in the project, or in the user folder)
#     whose frontmatter pins `model:` and `effort:` to one of the three pairs (for example `stock-verifier`).
# Built-in types (Explore, Plan, general-purpose) and plugin agents therefore need explicit parameters.
#
# Scope: this checks the parameters Claude passes. It cannot see the model of the main session (that is
# `modelSettings` in the user's settings.json) or agents that a dynamic workflow starts (ultracode is
# against the policy anyway). Fails closed when it cannot read the payload.
#
# Tests: evals/agent_model_cases.tsv with evals/run_agent_model_cases.sh.

PATH="/usr/bin:/bin:$PATH"
export PATH
set -f

block() {
  echo "Blocked by project rule: model policy ($1). Allowed pairs: opus+high, opus+medium, haiku+xhigh (haiku+medium only for the browser agents stock-verifier and browser-runner); set both model and effort on the Agent call." >&2
  exit 2
}

payload=""
while IFS= read -r line || [ -n "$line" ]; do
  payload="$payload$line"
done

[ "$(printf 'x' | sed 's/x/y/' 2>/dev/null)" = "y" ] || block "hook self-test failed: sed"
[ "$(printf 'x\n' | awk '{print $1}' 2>/dev/null)" = "x" ] || block "hook self-test failed: awk"
[ -n "$payload" ] || block "empty hook payload"

# Value of a flat JSON string field of tool_input. Quotes inside other strings are escaped in JSON (\"),
# so text inside the prompt cannot fake a field.
field() {
  printf '%s' "$payload" | sed -n "s/.*\"$1\"[[:space:]]*:[[:space:]]*\"\([^\"]*\)\".*/\1/p" | head -n 1
}

# Value of a frontmatter key of an agent definition file.
frontmatter() {
  awk -v k="$2" '
    { sub(/\r$/, "") }
    NR == 1 && $0 != "---" { exit }
    NR > 1 && $0 == "---" { exit }
    NR > 1 { i = index($0, ":"); if (i > 0 && substr($0, 1, i - 1) == k) { v = substr($0, i + 1); gsub(/^[ \t]+|[ \t]+$/, "", v); print v; exit } }
  ' "$1"
}

family() {
  case "$1" in
    opus|claude-opus-5-5) echo opus ;;
    haiku|claude-haiku-5-5) echo haiku ;;
    *) echo "" ;;
  esac
}

BROWSER_AGENTS=" stock-verifier browser-runner "

# Whether an effort is allowed for a model family ($3: the subagent type, for the browser pair).
allowed_pair() {
  case "$1:$2" in
    opus:high|opus:medium|haiku:xhigh) return 0 ;;
    haiku:medium) case "$BROWSER_AGENTS" in *" $3 "*) return 0 ;; esac ;;
  esac
  return 1
}

lower() { printf '%s' "$1" | tr 'A-Z' 'a-z'; }

model="$(lower "$(field model)")"
effort="$(lower "$(field effort)")"
stype="$(field subagent_type)"

if [ -z "$model" ] && [ -z "$effort" ]; then
  [ "$stype" = "fork" ] && exit 0
  if [ -n "$stype" ]; then
    for dir in "${CLAUDE_PROJECT_DIR:-.}/.claude/agents" "${CLAUDE_USER_DIR:-$HOME/.claude}/agents"; do
      file="$dir/$stype.md"
      if [ -f "$file" ]; then
        m="$(lower "$(frontmatter "$file" model)")"
        e="$(lower "$(frontmatter "$file" effort)")"
        fam="$(family "$m")"
        if [ -n "$fam" ] && allowed_pair "$fam" "$e" "$stype"; then
          exit 0
        fi
        block "the definition of agent '$stype' must pin model and effort to an allowed pair"
      fi
    done
  fi
  block "no model and no effort were set"
fi

fam="$(family "$model")"
[ -n "$fam" ] || block "model '${model:-none}' is not allowed"
allowed_pair "$fam" "$effort" "$stype" || block "$fam cannot run at effort '${effort:-none}'"
exit 0
