#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

usage() {
  cat <<'EOF'
Usage:
  scripts/lean-ci-local.sh [--bootstrap] [--clean] [Lake target ...]

Examples:
  scripts/lean-ci-local.sh --bootstrap
  scripts/lean-ci-local.sh
  scripts/lean-ci-local.sh Formal.R3SchwartzNormFieldL2
  scripts/lean-ci-local.sh --clean

Modes:
  --bootstrap  Install Elan if needed, resolve pinned Lake dependencies, and fetch the mathlib cache.
  --clean      Remove only this project's .lake/build directory before building.

Without a target, this runs the same default `lake build` target as GitHub Actions.
With one or more targets, Lake builds only those targets and their dependencies.
EOF
}

bootstrap=0
clean=0
targets=()

while (($#)); do
  case "$1" in
    --bootstrap) bootstrap=1 ;;
    --clean) clean=1 ;;
    -h|--help) usage; exit 0 ;;
    *) targets+=("$1") ;;
  esac
  shift
done

echo "==> Reject proof holes and local axioms"
if grep -RInE --include='*.lean' '(^|[^[:alnum:]_])(sorry|admit)([^[:alnum:]_]|$)' Formal; then
  echo 'ERROR: proof hole token detected under Formal/.' >&2
  exit 1
fi
if grep -RInE --include='*.lean' '^[[:space:]]*(axiom|opaque)[[:space:]]' Formal; then
  echo 'ERROR: local axiom/opaque declaration detected under Formal/.' >&2
  exit 1
fi

if ! command -v elan >/dev/null 2>&1; then
  if [[ "$bootstrap" != 1 ]]; then
    echo "ERROR: elan is not installed. Re-run with --bootstrap." >&2
    exit 2
  fi
  echo "==> Install Elan"
  curl --retry 3 --retry-all-errors --retry-delay 2 \
    https://elan.lean-lang.org/elan-init.sh -sSf | sh -s -- -y
  export PATH="$HOME/.elan/bin:$PATH"
fi

# `lean-toolchain` pins the exact Lean release. Invoking Lean/ Lake through Elan
# installs it on first use and then reuses it on later local runs.
echo "==> Toolchain"
lean --version
lake --version

if [[ "$bootstrap" == 1 ]]; then
  echo "==> Resolve pinned Lake dependencies"
  # mathlib's post-update hook already fetches the mathlib olean cache for
  # downstream projects. Do not immediately run a second redundant cache get.
  lake update
elif [[ ! -d .lake/packages/mathlib ]]; then
  echo "ERROR: Lake dependencies are not present. Re-run with --bootstrap." >&2
  exit 2
fi

if [[ "$clean" == 1 ]]; then
  echo "==> Remove project build artifacts (.lake/build only)"
  rm -rf .lake/build
fi

if ((${#targets[@]} == 0)); then
  echo "==> Full formalization build"
  lake build
else
  echo "==> Targeted build: ${targets[*]}"
  lake build "${targets[@]}"
fi
