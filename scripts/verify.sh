#!/usr/bin/env bash
#
# One command that is a superset of CI. Run it before reporting that a change is done.
#
# Ported from Winged-Swift/Scripts/verify.sh, including its two best ideas: accumulate
# failures instead of stopping at the first one, so a single run reports every problem;
# and finish with an end-to-end smoke test that installs this checkout into a throwaway
# environment and renders a real page, proving the library is actually consumable rather
# than merely importable.

set -uo pipefail

RED=$'\033[0;31m'; GREEN=$'\033[0;32m'; BLUE=$'\033[0;34m'; YELLOW=$'\033[1;33m'; RESET=$'\033[0m'
FAILURES=0
LOG=$(mktemp)
trap 'rm -f "$LOG"' EXIT

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PY="${PYTHON:-python3}"

step() { printf '\n%s==> %s%s\n' "$BLUE" "$1" "$RESET"; }
ok()   { printf '%s  ok%s    %s\n' "$GREEN" "$RESET" "$1"; }
fail() { printf '%s  FAIL%s  %s\n' "$RED" "$RESET" "$1"; FAILURES=$((FAILURES + 1)); }

run() {
  local label="$1"; shift
  if "$@" > "$LOG" 2>&1; then
    ok "$label"
  else
    fail "$label"
    sed 's/^/        /' "$LOG" | tail -40
  fi
}

step "1/7  Build"
run "python -m build" "$PY" -m build --outdir "$ROOT/.verify-dist"
if ls "$ROOT"/.verify-dist/*.whl > /dev/null 2>&1; then
  WHEEL=$(ls "$ROOT"/.verify-dist/*.whl | head -1)
  if "$PY" -c "import zipfile,sys; sys.exit(0 if 'winged/py.typed' in zipfile.ZipFile('$WHEEL').namelist() else 1)"; then
    ok "wheel ships winged/py.typed"
  else
    fail "wheel is missing winged/py.typed — consumers would get no types"
  fi
fi

step "2/7  Test"
run "pytest" "$PY" -m pytest -q

step "3/7  Lint and types"
run "ruff check" "$PY" -m ruff check .
run "ruff format --check" "$PY" -m ruff format --check .
run "mypy --strict" "$PY" -m mypy

step "4/7  Generated files are current"
run "elements.py"     "$PY" scripts/generate_elements.py --check
run "tag-catalog.md"  "$PY" scripts/generate_tag_catalog.py --check

step "5/7  Golden fixtures"
# Deliberately without WINGED_UPDATE_FIXTURES: a stale fixture must be a failure here,
# never a silent rewrite.
run "parity with Winged-Swift" "$PY" -m pytest tests/test_golden.py -q --no-cov

step "6/7  End-to-end consumer smoke test"
SMOKE=$(mktemp -d)
{
  "$PY" -m venv "$SMOKE/venv" \
    && "$SMOKE/venv/bin/pip" install --quiet "$ROOT" \
    && cat > "$SMOKE/render.py" <<'PYEOF'
from winged import Body, Document, H1, Head, P, Title, render

page = Document(Head(Title("Smoke")), Body(H1("Winged"), P("<ok>")))
print(render(page))
PYEOF
  "$SMOKE/venv/bin/python" "$SMOKE/render.py" > "$SMOKE/out.html"
} > "$LOG" 2>&1

if [ -s "$SMOKE/out.html" ] \
  && grep -q '<!DOCTYPE html>' "$SMOKE/out.html" \
  && grep -q '<h1>Winged</h1>' "$SMOKE/out.html" \
  && grep -q '&lt;ok&gt;' "$SMOKE/out.html"; then
  ok "installed package renders, and escapes its content"
else
  fail "end-to-end render"
  sed 's/^/        /' "$LOG" | tail -30
  sed 's/^/        /' "$SMOKE/out.html" 2>/dev/null | tail -10
fi

step "7/7  CLI smoke test"
# Run from / on purpose. A generator that resolves its paths from the current directory
# passes every unit test and still fails for the user; this is the only check that notices.
CLI=$(mktemp -d)
if [ -x "$SMOKE/venv/bin/winged" ]; then
  (cd / && "$SMOKE/venv/bin/winged" new smoke --path "$CLI/smoke" \
    && cd "$CLI/smoke" && "$SMOKE/venv/bin/winged" build) > "$LOG" 2>&1

  MISSING=""
  for artifact in dist/index.html dist/css/style.css dist/sitemap.xml AGENTS.md; do
    [ -f "$CLI/smoke/$artifact" ] || MISSING="$MISSING $artifact"
  done
  if [ -z "$MISSING" ]; then
    ok "winged new + winged build, run from /"
  else
    fail "winged CLI did not produce:$MISSING"
    sed 's/^/        /' "$LOG" | tail -30
    printf '        %s\n' "$("$PY" -VV)" "$(uname -a)"
  fi
else
  fail "the winged entry point was not installed"
fi

rm -rf "$SMOKE" "$CLI" "$ROOT/.verify-dist"

printf '\n'
if [ "$FAILURES" -eq 0 ]; then
  printf '%sEverything passed.%s\n' "$GREEN" "$RESET"
  exit 0
fi
printf '%s%d step(s) failed.%s\n' "$RED" "$FAILURES" "$RESET"
exit 1
