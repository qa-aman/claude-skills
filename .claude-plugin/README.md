# Plugin manifests (maintainers)

This directory turns the repository into both a Claude Code **plugin marketplace** and the single
**plugin** that marketplace publishes. It is what makes `/plugin marketplace add qa-aman/claude-skills`
followed by `/plugin install claude-skills@claude-skills` work, and it is what gives users an update
path that the clone-and-run-the-script method does not have.

Nothing in here changes how the skills themselves behave. It only describes them to Claude Code.

## The two files

1. `marketplace.json` is the catalog. Required fields are `name`, `owner` and `plugins`. Every entry
   in `plugins` needs at least a `name` and a `source`. Ours uses `"source": "./"`, which means the
   plugin is the marketplace repository itself.
2. `plugin.json` is the plugin manifest. `name` is the only required field. It carries the version,
   description, author, licence and the list of skill directories.

Both files must live inside `.claude-plugin/`. Everything else, including `skills/`, stays at the
repository root. Putting a component directory inside `.claude-plugin/` is the most common reason a
plugin loads with nothing in it.

## Why the skills paths are listed one by one

The default plugin scan looks for `skills/<name>/SKILL.md`. This repo nests one level deeper,
`skills/by-role/<role>/<name>/SKILL.md` and `skills/shared/<name>/SKILL.md`, so the default scan
finds nothing. The `skills` field takes custom directories that contain `<name>/SKILL.md`, so both
manifests list `./skills/shared` plus one path per role directory.

Note the documented behaviour for a marketplace entry whose `source` resolves to the marketplace
root: the listed paths become the complete set for that entry and replace the default `skills/`
scan. That is exactly what we want here. The same list is repeated in `plugin.json` so the plugin
also loads correctly when tested directly with `claude --plugin-dir .`.

## What to update when a skill is added

1. Add the skill under `skills/by-role/<role>/<name>/SKILL.md` or `skills/shared/<name>/SKILL.md`.
2. Register it in `skills.json` (the scaffold script does this).
3. Add a row to `VERSIONS.md` at 1.0.0 with today's date in DD-MM-YYYY.
4. Update the skills table and the skill count in `README.md`.
5. Only if the skill introduces a **new role directory**, add `./skills/by-role/<new-role>` to the
   `skills` array in both `plugin.json` and `marketplace.json`. An added skill inside an existing
   role needs no manifest change, because the role directory is already listed.
6. Bump `version` in both `plugin.json` and the `marketplace.json` plugin entry. Users only receive
   updates when that string changes, so a release without a bump is invisible to them.

Validate before pushing:

```bash
python3 -c "import json; json.load(open('.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json'))"
claude plugin validate .
```

## Reference docs

1. Plugin manifest schema, skills discovery, path behaviour rules:
   https://code.claude.com/docs/en/plugins-reference
2. Marketplace schema, plugin entries, plugin sources, hosting on GitHub:
   https://code.claude.com/docs/en/plugin-marketplaces
3. Creating plugins, directory layout, local testing with `--plugin-dir`:
   https://code.claude.com/docs/en/plugins
4. What users run to find and install a plugin:
   https://code.claude.com/docs/en/discover-plugins
