#!/bin/sh
# PreToolUse hook (Agent): the model policy (owner decisions 2026-10-25 and 2026-11-07).
#
# Only three model + effort pairs are allowed on an Agent call:
#   opus + high      the hardest, most delicate or "we cannot fail" work
#   opus + medium    planning, orchestration, general chat, code (medium work)
#   haiku + xhigh    repetitive and light work
# plus one special pair for driving the browser (owner, 2026-11-07, on trial): haiku + medium, only for the
# browser agents listed in BROWSER_AGENTS.
# plus Fable 5.2 (owner, 2026-11-14), ONLY with his explicit OK: his message "autorizo fable [effort]" makes the
# UserPromptSubmit hook write `.claude/fable-authorization` ("<UTC time> <effort>"); fable is allowed at that effort
# with no expiry (owner, 2026-11-15) and blocked without the file. The hook only records that Fable is enabled: Claude
# still launches Fable ONLY on the owner's explicit OK for that run, never on a guess (CLAUDE.md model policy).
# plus Opus 5.5 at effort max (owner, 2026-11-21), ONLY with his message "autorizo opus max": the UserPromptSubmit hook
# writes `.claude/opus-max-authorization`; one Agent call on opus+max is allowed within 30 minutes and uses it up.
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
  echo "Blocked by project rule: model policy ($1). Allowed pairs: opus+high, opus+medium, haiku+xhigh (haiku+medium only for the browser agents stock-verifier and browser-runner; fable only at the effort the owner authorized with 'autorizo fable', and only on his explicit OK for the run; opus+max only once per 'autorizo opus max'); set both model and effort on the Agent call." >&2
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
    fable|claude-fable-5-2) echo fable ;;
    *) echo "" ;;
  esac
}

BROWSER_AGENTS=" stock-verifier browser-runner "
FABLE_TOKEN="${FABLE_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/fable-authorization}"
OPUS_MAX_TOKEN="${OPUS_MAX_TOKEN_FILE:-${CLAUDE_PROJECT_DIR:-.}/.claude/opus-max-authorization}"

# Whether the owner's one-shot Opus max authorization exists and is younger than 30 minutes.
opus_max_authorized() {
  [ -f "$OPUS_MAX_TOKEN" ] || return 1
  [ -n "$(find "$OPUS_MAX_TOKEN" -mmin -30 2>/dev/null)" ]
}

# Whether the owner's Fable authorization is on record for this effort (no expiry, owner 2026-11-15).
fable_authorized() {
  [ -f "$FABLE_TOKEN" ] || return 1
  [ "$(awk '{print tolower($2); exit}' "$FABLE_TOKEN")" = "$1" ]
}

# Whether an effort is allowed for a model family ($3: the subagent type, for the browser pair).
allowed_pair() {
  case "$1:$2" in
    opus:high|opus:medium|haiku:xhigh) return 0 ;;
    haiku:medium) case "$BROWSER_AGENTS" in *" $3 "*) return 0 ;; esac ;;
    fable:*) fable_authorized "$2" && return 0 ;;
    opus:max) opus_max_authorized && rm -f "$OPUS_MAX_TOKEN" && return 0 ;;
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
