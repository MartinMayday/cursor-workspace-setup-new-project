# Cursor IDE Workspace Setup - Complete Package

This package provides a comprehensive, interview-driven framework for setting up Cursor IDE workspace configuration for new projects.

## 📦 What's Included

1. **SOP-Cursor-Workspace-Setup.md** - Complete Standard Operating Procedure with 5-phase interview framework
2. **setup_cursor_workspace.py** - Automated execution script that scaffolds workspace from interview record
3. **source_list.json.template** - Template for local knowledge base with documentation references

## 🚀 Quick Start

### Step 1: Conduct Interview

Use the 5-phase interview framework from `SOP-Cursor-Workspace-Setup.md`:

1. **Phase 1: Project Classification** - What type of project?
2. **Phase 2: Technology Stack & Architecture** - What services/technologies?
3. **Phase 3: Constraints & Requirements** - What are critical constraints?
4. **Phase 4: Development Workflow & Standards** - What coding standards?
5. **Phase 5: Confirmation & Examples** - Correct vs. incorrect examples

### Step 2: Fill Interview Record

Copy the Context Extraction Template from the SOP and fill it with interview findings. Save as `interview-record.md`.

### Step 3: Run Execution Script

```bash
# Navigate to project root
cd /path/to/your/project

# Run the script
python3 setup_cursor_workspace.py \
  --interview-record interview-record.md \
  --project-path . \
  --template-dir .cursor/templates
```

### Step 4: Validate & Review

1. Review generated `.cursorrules`
2. Test commands in `.cursor/commands/`
3. Validate rules match your project structure
4. Commit to version control

## 📋 Prerequisites

- Python 3.12+
- Completed interview record (Context Extraction Template filled)
- Project root directory identified
- Template files (optional - script creates minimal templates if missing)

## 🎯 Expected Output

After running the script, you'll have:

- `.cursorrules` - Main workspace rules
- `.cursor/rules/*.mdc` - Project-specific rules
- `.cursor/commands/**/*.md` - Development commands
- `.cursor/AGENTS.md` - Agent configuration
- `.cursor/rules/rules_manifest.json` - Progressive context loading manifest
- `.cursor/commands/commands_manifest.json` - Commands manifest
- `.cursor/hooks/hooks_manifest.json` - Hooks manifest
- `source_list.json` - Local knowledge base with documentation references

## 🔍 Key Features

### Interview-Driven Approach

The framework uses a structured 5-phase interview to extract all necessary context:
- No assumptions made
- All variables explicitly extracted
- Examples provided (correct vs. incorrect)
- Validation before generation

### Zero-Assumption Principles

- All recommendations cite sources
- Reference files protected (never modify originals)
- Project-specific adaptation (no generic templates)
- Runtime verification protocols

### Automated Scaffolding

- Template-based file generation
- Placeholder replacement with extracted context
- Directory structure creation
- Validation and error checking

## 📚 Documentation References

The `source_list.json` includes references to:

- **Cursor IDE**: Rules, commands, ignore files
- **Claude**: Code documentation, agents SDK
- **Docker & OrbStack**: Container deployment
- **MCP**: Model Context Protocol
- **Languages**: Python, TypeScript, JavaScript
- **Frameworks**: React, Vite, FastAPI
- **Tools**: Ruff, MyPy, Pytest, Vitest, ESLint, Biome
- **Databases**: Supabase, PostgreSQL
- **Best Practices**: TDD, Agile, Project Management, SDD
- **Standards**: Project scaffolding, file generation discipline

## 🛠️ Customization

### Adding Custom Templates

1. Create template files in `.cursor/templates/`
2. Use `<PLACEHOLDER: KEY>` syntax for replacement
3. Script will automatically process all `.template` files

### Extending source_list.json

Add new sources to `source_list.json.template` following the existing format:
- `id`: Unique identifier
- `title`: Human-readable title
- `url`: Documentation URL
- `type`: official_docs | sdk | best_practices
- `trust_level`: high | medium | low
- `key_facts`: Array of important facts
- `use_when`: Array of use cases

## 📖 Learn More

- Read `SOP-Cursor-Workspace-Setup.md` for complete framework documentation
- Review interview examples in the SOP
- Check validation checklist before committing

## 🐛 Troubleshooting

### Script Fails with "Missing required context variables"

**Solution**: Complete the interview record with all required variables:
- `project_name`
- `project_type`
- `services`

### Generated files don't match project structure

**Solution**: Review interview record and ensure all placeholders are filled correctly. Re-run interview if needed.

### Template directory not found

**Solution**: Script will create minimal templates automatically. For custom templates, create `.cursor/templates/` directory.

## 📝 License

Internal Use — Enterprise Operations

---

*This framework is designed for teams building production systems where reliability and predictability are non-negotiable.*

