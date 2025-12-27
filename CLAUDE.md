# Claude Configuration — Cursor Workspace Setup Framework

This document provides Claude-specific configuration and guidelines for working with the Cursor Workspace Setup Framework.

## Framework Purpose

The Cursor Workspace Setup Framework uses a structured, interview-driven approach to extract project context and automatically scaffold Cursor IDE workspace configurations. This ensures zero-assumption principles are followed and all workspace configurations are tailored to specific project needs.

## Key Concepts

### Interview-Driven Methodology

The framework uses a 5-phase interview process:

1. **Project Classification** — Determine project type and primary technology stack
2. **Technology Stack & Architecture** — Extract services, technologies, and architecture patterns
3. **Constraints & Requirements** — Identify deployment, networking, and integration constraints
4. **Development Workflow & Standards** — Extract coding standards and file organization patterns
5. **Confirmation & Examples** — Confirm understanding and gather correct/incorrect examples

### Zero-Assumption Principles

- **Always reference official documentation** before making recommendations
- **Cite sources** for all architectural decisions
- **Never proceed without documentation backing**
- **Extract all variables explicitly** — no guessing

### Reference File Protection

**CRITICAL**: Never modify original reference files from example configurations.

- **READ-ONLY** — Never modified, only referenced for context
- **Context source only** — Extract principles, strategies, structures, patterns
- **Generate new files** — Create project-specific files, don't modify originals
- **Project-specific adaptation** — Adapt principles to project context, don't copy verbatim

## Working with the Framework

### When to Use This Framework

Use this framework when:
- Setting up Cursor IDE workspace for a new project
- Migrating existing project to Cursor IDE
- Standardizing workspace configuration across team
- Ensuring zero-assumption principles are followed

### How to Use This Framework

1. **Conduct Interview**: Use the 5-phase interview framework from `SOP-Cursor-Workspace-Setup.md`
2. **Fill Template**: Document findings in Context Extraction Template
3. **Run Script**: Execute `setup_cursor_workspace.py` with interview record
4. **Validate**: Review generated files against checklist
5. **Commit**: Add to version control

### Key Files

- `SOP-Cursor-Workspace-Setup.md` — Complete framework documentation
- `setup_cursor_workspace.py` — Automated scaffolding script
- `source_list.json.template` — Knowledge base template
- `README.md` — Quick start guide

## Claude-Specific Guidelines

### When Generating Workspace Configurations

1. **Follow Interview Framework**: Always use the 5-phase interview process
2. **Extract Variables Explicitly**: Document all findings in template
3. **Use Placeholders**: Mark project-specific content with `<PLACEHOLDER: KEY>`
4. **Provide Examples**: Include correct and incorrect examples
5. **Validate Output**: Check against validation checklist

### When Modifying Framework Files

1. **Protect Reference Files**: Never modify original example files
2. **Update Templates**: Modify template files, not generated outputs
3. **Document Changes**: Update relevant documentation
4. **Test Script**: Verify script still works after changes

### When Helping Users

1. **Guide Through Interview**: Help conduct 5-phase interview
2. **Extract Context**: Assist in filling Context Extraction Template
3. **Run Script**: Execute setup script with proper parameters
4. **Validate Results**: Review generated files for correctness
5. **Troubleshoot Issues**: Help resolve any problems

## Common Patterns

### Microservices Project

- Extract each service with technology stack and port
- Document inter-service communication patterns
- Specify container naming conventions
- Define networking requirements (Traefik, direct ports, etc.)

### Monorepo Project

- List all packages with purposes
- Document dependency management strategy
- Specify package organization pattern
- Define inter-package reference patterns

### Full-Stack Application

- Extract frontend and backend stacks separately
- Document API communication patterns
- Specify deployment strategy
- Define testing requirements for both stacks

## Best Practices

### Interview Process

- **One question at a time** — Don't rush through phases
- **Adaptive questioning** — Adjust based on project type
- **Confirm understanding** — Recap before proceeding
- **Gather examples** — Request concrete correct/incorrect examples

### Script Execution

- **Validate first** — Check interview record completeness
- **Review output** — Verify placeholder replacements
- **Test commands** — Ensure generated commands work
- **Document customizations** — Note any manual adjustments

### Maintenance

- **Update templates** — Keep templates current with best practices
- **Extend knowledge base** — Add new documentation references
- **Improve examples** — Enhance wrong/correct examples
- **Version control** — Track all changes

## Troubleshooting

### Interview Record Incomplete

**Symptoms**: Script fails with "Missing required context variables"

**Solution**: 
- Review interview record for missing variables
- Re-conduct interview phases if needed
- Ensure all placeholders are filled

### Generated Files Incorrect

**Symptoms**: Generated files don't match project structure

**Solution**:
- Review interview record for accuracy
- Check placeholder replacements
- Verify template files are correct
- Re-run script after corrections

### Script Errors

**Symptoms**: Python script throws exceptions

**Solution**:
- Check Python version (3.12+ required)
- Verify interview record format
- Check template file syntax
- Review error messages for specific issues

## Resources

- **Framework SOP**: `SOP-Cursor-Workspace-Setup.md`
- **Quick Start**: `README-Workspace-Setup.md`
- **Package Overview**: `DELIVERABLES-SUMMARY.md`
- **Agent Guide**: `AGENTS.md`

## Version

**Version**: 1.0 Enterprise  
**Last Updated**: 2025-01-XX  
**Status**: Production Ready

---

*This framework is designed for teams building production systems where reliability and predictability are non-negotiable.*

