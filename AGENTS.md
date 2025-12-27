# Agents Guide — Cursor Workspace Setup Framework

Repo root: `/Volumes/uss/homelab/containers/homelab-core/components/cursor-workspace-setup-new-project`

## Operating Rules

- **Generated artifacts**: Put new, AI-generated files in `.cursor/tmp/` (fallback: `tmp/`) unless the user requests otherwise.
- **Repo boundary**: Do not modify files outside this repo unless explicitly asked.
- **Secrets**: Never add secrets/tokens/keys to the repo. Prefer untracked `.env` files or Docker secrets.
- **Networking**: Use real, network-resolvable hostnames; do not introduce `localhost`, `127.0.0.1`, `::1`, `0.0.0.0` unless explicitly requested.
- **Reference files**: NEVER modify original reference files from example configurations. Only copy context (principles, strategies, structures).

## Key Files in This Repo

- `SOP-Cursor-Workspace-Setup.md` — Complete Standard Operating Procedure with 5-phase interview framework
- `setup_cursor_workspace.py` — Automated execution script for workspace scaffolding
- `source_list.json.template` — Template for local knowledge base with documentation references
- `README.md` — Project overview and quick start guide
- `AGENTS.md` — This file (agent configuration guide)
- `CLAUDE.md` — Claude-specific configuration and guidelines

## Framework Overview

This framework provides a structured, interview-driven approach to setting up Cursor IDE workspaces:

### Five-Phase Interview Flow

1. **Phase 1: Project Classification** — Determine project type (microservices, monorepo, SPA, etc.)
2. **Phase 2: Technology Stack & Architecture** — Extract services, technologies, ports
3. **Phase 3: Constraints & Requirements** — Identify deployment, networking, database constraints
4. **Phase 4: Development Workflow & Standards** — Extract coding standards, file organization, testing
5. **Phase 5: Confirmation & Examples** — Confirm understanding and gather correct/incorrect examples

### Execution Script

The `setup_cursor_workspace.py` script:
- Parses interview record markdown
- Extracts context variables
- Validates required variables
- Loads template files
- Replaces placeholders with extracted context
- Generates complete workspace structure
- Creates manifest files
- Generates source_list.json

## Development Commands

### Running the Setup Script

```bash
python3 setup_cursor_workspace.py \
  --interview-record interview-record.md \
  --project-path . \
  --template-dir .cursor/templates
```

### Creating Interview Record

1. Copy Context Extraction Template from `SOP-Cursor-Workspace-Setup.md`
2. Conduct 5-phase interview with stakeholder
3. Fill in template with extracted variables
4. Save as `interview-record.md`

## Code Quality Standards

### Python Script

- **Python 3.12+** with type hints
- **120 character line length**
- **Docstrings** for all functions
- **Error handling** with clear messages

### Documentation

- **Markdown** format for all docs
- **Placeholders** marked with `<PLACEHOLDER: KEY>` syntax
- **Examples** included for all concepts
- **Validation checklists** for quality assurance

## Best Practices

### Interview Process

- **One question at a time** — Wait for response before proceeding
- **Adaptive questioning** — Adjust questions based on project type
- **Extract variables** — Document all findings in template
- **Confirm understanding** — Recap before moving to next phase
- **Gather examples** — Request correct and incorrect examples

### Script Usage

- **Validate interview record** — Ensure all required variables present
- **Review generated files** — Check for placeholder replacements
- **Test commands** — Verify generated commands work
- **Commit to version control** — Track workspace configuration

## Troubleshooting

### Script Fails with "Missing required context variables"

**Solution**: Complete the interview record with all required variables:
- `project_name`
- `project_type`
- `services`

### Generated Files Don't Match Project Structure

**Solution**: Review interview record and ensure all placeholders are filled correctly. Re-run interview if needed.

### Template Directory Not Found

**Solution**: Script will create minimal templates automatically. For custom templates, create `.cursor/templates/` directory.

## Resources

- **SOP Documentation**: `SOP-Cursor-Workspace-Setup.md`
- **Quick Start**: `README-Workspace-Setup.md`
- **Package Overview**: `DELIVERABLES-SUMMARY.md`
- **Knowledge Base**: `source_list.json.template`

## Guardrails

- Avoid modifying original reference files from examples
- Prefer updating existing documentation over creating new redundant docs
- Always validate generated files before committing
- Follow zero-assumption principles — cite sources for all recommendations

