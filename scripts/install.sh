#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_SKILLS_DIR="$SCRIPT_DIR/../skills"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

AVAILABLE_SKILLS=(
  linkedin-post
  reddit-post
  newsletter-ideation
  substack-post
  substack-notes
  substack-toc
  presentation-builder
  11-star-framework
)

usage() {
  echo "Usage: $0 [--all | skill-name ...]"
  echo ""
  echo "Install Claude Code skills into $TARGET_DIR"
  echo ""
  echo "Options:"
  echo "  --all              Install all skills"
  echo "  --list             List available skills"
  echo "  --target DIR       Override target directory (default: ~/.claude/skills)"
  echo ""
  echo "Available skills:"
  for skill in "${AVAILABLE_SKILLS[@]}"; do
    echo "  $skill"
  done
}

install_skill() {
  local skill="$1"
  local src="$REPO_SKILLS_DIR/$skill"
  local dest="$TARGET_DIR/$skill"

  if [ ! -d "$src" ]; then
    echo "Error: skill '$skill' not found in $REPO_SKILLS_DIR"
    return 1
  fi

  mkdir -p "$dest"
  cp -r "$src"/* "$dest"/
  echo "Installed: $skill -> $dest"
}

if [ $# -eq 0 ]; then
  usage
  exit 1
fi

# Parse args
SKILLS_TO_INSTALL=()

while [ $# -gt 0 ]; do
  case "$1" in
    --all)
      SKILLS_TO_INSTALL=("${AVAILABLE_SKILLS[@]}")
      shift
      ;;
    --list)
      for skill in "${AVAILABLE_SKILLS[@]}"; do
        echo "$skill"
      done
      exit 0
      ;;
    --target)
      TARGET_DIR="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      SKILLS_TO_INSTALL+=("$1")
      shift
      ;;
  esac
done

if [ ${#SKILLS_TO_INSTALL[@]} -eq 0 ]; then
  echo "No skills specified. Use --all or provide skill names."
  exit 1
fi

mkdir -p "$TARGET_DIR"

installed=0
for skill in "${SKILLS_TO_INSTALL[@]}"; do
  if install_skill "$skill"; then
    ((installed++))
  fi
done

echo ""
echo "Done. $installed skill(s) installed to $TARGET_DIR"
