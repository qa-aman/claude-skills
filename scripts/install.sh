#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$SCRIPT_DIR/.."
SKILLS_DIR="$REPO_DIR/skills"
REGISTRY="$REPO_DIR/skills.json"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

if ! command -v python3 &>/dev/null; then
  echo "Error: python3 is required"
  exit 1
fi

get_skills_for_role() {
  local role="$1"
  python3 - <<EOF
import json
data = json.load(open('$REGISTRY'))
for key, val in data['skills'].items():
    if val['role'] == '$role':
        print(key)
EOF
}

get_shared_skills() {
  python3 - <<EOF
import json
data = json.load(open('$REGISTRY'))
for key, val in data['skills'].items():
    if val['role'] == 'shared':
        print(key)
EOF
}

get_all_skills() {
  python3 - <<EOF
import json
data = json.load(open('$REGISTRY'))
for key in data['skills']:
    print(key)
EOF
}

get_all_roles() {
  python3 - <<EOF
import json
data = json.load(open('$REGISTRY'))
roles = sorted(set(v['role'] for v in data['skills'].values() if v['role'] != 'shared'))
for r in roles:
    print(r)
EOF
}

install_skill() {
  local skill_key="$1"
  local role
  role="$(dirname "$skill_key")"
  local name
  name="$(basename "$skill_key")"

  local src
  if [ "$role" = "shared" ]; then
    src="$SKILLS_DIR/shared/$name"
  else
    src="$SKILLS_DIR/by-role/$skill_key"
  fi

  if [ ! -d "$src" ]; then
    echo "  Error: '$skill_key' not found at $src"
    return 1
  fi

  local dest="$TARGET_DIR/$name"
  mkdir -p "$dest"
  cp -r "$src"/. "$dest"/
  echo "  Installed: $name"
}

uninstall_role() {
  local role="$1"
  while IFS= read -r skill_key; do
    local name
    name="$(basename "$skill_key")"
    local dest="$TARGET_DIR/$name"
    if [ -d "$dest" ]; then
      rm -rf "$dest"
      echo "  Removed: $name"
    fi
  done < <(get_skills_for_role "$role")
}

init_context() {
  local context_file="$TARGET_DIR/skill-context.md"
  if [ -f "$context_file" ]; then
    echo "skill-context.md already exists at $context_file"
    echo "Edit it directly to update your context."
    return
  fi

  local template="$REPO_DIR/skill-context.example.md"
  mkdir -p "$TARGET_DIR"

  if [ -f "$template" ]; then
    cp "$template" "$context_file"
    echo "Created: $context_file"
    echo "Fill in your values - skills read this file at invocation time."
    echo "Open it with: open $context_file"
  else
    # Fallback if template missing
    cat > "$context_file" <<CONTEXT
# Skill Context
# Skills read this file at invocation time to personalize their output.
# Edit anytime - skills never modify this file.

- Industry: [e.g. Fintech, EdTech, SaaS]
- Stack: [e.g. React + Node.js]
- Compliance: [e.g. PCI-DSS, HIPAA, or none]
- Defect tracker: [e.g. Jira, Linear, GitHub Issues]
- Test framework: [e.g. Jest, Cypress, Playwright]
CONTEXT
    echo "Created: $context_file"
    echo "Fill in your values - skills read this file at invocation time."
  fi
}

list_skills() {
  echo "Available skills:"
  echo ""
  while IFS= read -r role; do
    echo "  [$role]"
    while IFS= read -r skill_key; do
      local name
      name="$(basename "$skill_key")"
      echo "    - $name"
    done < <(get_skills_for_role "$role")
  done < <(get_all_roles)
  echo ""
  echo "  [shared]"
  while IFS= read -r skill_key; do
    local name
    name="$(basename "$skill_key")"
    echo "    - $name"
  done < <(get_shared_skills)
}

usage() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  --role ROLE[,ROLE]   Install skills for one or more roles (also installs shared)"
  echo "  --all                Install all skills"
  echo "  --update             Re-install all currently installed skills"
  echo "  --uninstall ROLE     Remove skills for a role"
  echo "  --init               Set up skill-context.md for personalization"
  echo "  --list               List all available skills by role"
  echo "  --target DIR         Override install directory (default: ~/.claude/skills)"
  echo "  --help               Show this help"
  echo ""
  echo "Examples:"
  echo "  $0 --role qa"
  echo "  $0 --role pm,content-creator"
  echo "  $0 --role qa --init"
  echo "  $0 --all"
  echo "  $0 --update"
  echo "  $0 --uninstall qa"
}

ROLES=()
DO_ALL=false
DO_UPDATE=false
DO_INIT=false
UNINSTALL_ROLE=""

if [ $# -eq 0 ]; then
  usage
  exit 1
fi

while [ $# -gt 0 ]; do
  case "$1" in
    --role)
      IFS=',' read -ra ROLES <<< "$2"
      shift 2
      ;;
    --all)
      DO_ALL=true
      shift
      ;;
    --update)
      DO_UPDATE=true
      shift
      ;;
    --uninstall)
      UNINSTALL_ROLE="$2"
      shift 2
      ;;
    --init)
      DO_INIT=true
      shift
      ;;
    --list)
      list_skills
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
      echo "Unknown option: $1"
      usage
      exit 1
      ;;
  esac
done

mkdir -p "$TARGET_DIR"

if [ -n "$UNINSTALL_ROLE" ]; then
  echo "Uninstalling $UNINSTALL_ROLE skills from $TARGET_DIR..."
  uninstall_role "$UNINSTALL_ROLE"
  echo "Done."
  exit 0
fi

SKILLS_TO_INSTALL=()

if [ "$DO_ALL" = true ] || [ "$DO_UPDATE" = true ]; then
  while IFS= read -r skill; do
    SKILLS_TO_INSTALL+=("$skill")
  done < <(get_all_skills)
elif [ ${#ROLES[@]} -gt 0 ]; then
  for role in "${ROLES[@]}"; do
    while IFS= read -r skill; do
      SKILLS_TO_INSTALL+=("$skill")
    done < <(get_skills_for_role "$role")
  done
  # Always include shared
  while IFS= read -r skill; do
    SKILLS_TO_INSTALL+=("$skill")
  done < <(get_shared_skills)
fi

if [ ${#SKILLS_TO_INSTALL[@]} -eq 0 ] && [ "$DO_INIT" = false ]; then
  echo "No skills to install. Use --role, --all, or --update."
  usage
  exit 1
fi

if [ ${#SKILLS_TO_INSTALL[@]} -gt 0 ]; then
  echo "Installing to $TARGET_DIR..."
  installed=0
  for skill in "${SKILLS_TO_INSTALL[@]}"; do
    if install_skill "$skill"; then
      ((installed++)) || true
    fi
  done
  echo ""
  echo "$installed skill(s) installed."
fi

if [ "$DO_INIT" = true ]; then
  echo ""
  init_context
fi
