#!/usr/bin/env python3
"""
Cursor IDE Workspace Setup Script
Automated scaffolding of Cursor workspace from interview record and templates.

Usage:
    python3 setup_cursor_workspace.py \
        --interview-record interview-record.md \
        --project-path . \
        --template-dir .cursor/templates

Requirements:
    - Python 3.12+
    - Interview record completed (Context Extraction Template filled)
    - Template files in template directory
"""

import argparse
import json
import os
import re
import shutil
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class CursorWorkspaceSetup:
    """Main class for Cursor workspace setup automation."""
    
    def __init__(self, interview_record_path: str, project_path: str, template_dir: str):
        self.interview_record_path = Path(interview_record_path)
        self.project_path = Path(project_path).resolve()
        self.template_dir = Path(template_dir)
        self.context: Dict[str, Any] = {}
        self.generated_files: List[str] = []
        
    def run(self):
        """Execute the complete workspace setup process."""
        print("🚀 Starting Cursor workspace setup...\n")
        
        # Phase 1: Parse interview record
        print("📖 Phase 1: Parsing interview record...")
        self.parse_interview_record()
        
        # Phase 2: Validate context
        print("✅ Phase 2: Validating extracted context...")
        self.validate_context()
        
        # Phase 3: Load templates
        print("📋 Phase 3: Loading templates...")
        templates = self.load_templates()
        
        # Phase 4: Generate files
        print("🔨 Phase 4: Generating workspace files...")
        self.generate_files(templates)
        
        # Phase 5: Validate output
        print("🔍 Phase 5: Validating generated files...")
        self.validate_output()
        
        # Phase 6: Report results
        print("\n" + "="*60)
        self.report_results()
        
    def parse_interview_record(self):
        """Parse the interview record markdown file and extract context variables."""
        if not self.interview_record_path.exists():
            raise FileNotFoundError(
                f"Interview record not found: {self.interview_record_path}"
            )
        
        content = self.interview_record_path.read_text()
        
        # Extract project metadata
        self.context['project_name'] = self._extract_placeholder(content, 'PROJECT_NAME', 'Untitled Project')
        self.context['project_path'] = str(self.project_path)
        self.context['date'] = datetime.now().strftime('%Y-%m-%d')
        
        # Extract Phase 1: Project Classification
        self.context['project_type'] = self._extract_placeholder(
            content, 'microservices | monorepo | spa | iac | data | api | fullstack', 'fullstack'
        )
        
        # Extract Phase 2: Technology Stack
        self.context['services'] = self._extract_services(content)
        self.context['frontend_stack'] = self._extract_placeholder(content, 'frontend_stack', '')
        self.context['backend_stack'] = self._extract_placeholder(content, 'backend_stack', '')
        self.context['database'] = self._extract_placeholder(content, 'database', '')
        self.context['deployment'] = self._extract_placeholder(content, 'deployment', 'docker_compose')
        self.context['architecture_pattern'] = self._extract_placeholder(
            content, 'architecture_pattern', 'monolith'
        )
        
        # Extract Phase 3: Constraints
        self.context['deployment_environment'] = self._extract_placeholder(
            content, 'homelab | cloud | hybrid | local', 'local'
        )
        self.context['networking'] = self._extract_networking(content)
        self.context['database_config'] = self._extract_database_config(content)
        self.context['secrets_management'] = self._extract_placeholder(
            content, 'secrets_management', '.env'
        )
        self.context['testing_requirements'] = self._extract_testing(content)
        self.context['hard_constraints'] = self._extract_list(content, 'hard_constraints')
        
        # Extract Phase 4: Development Standards
        self.context['coding_standards'] = self._extract_coding_standards(content)
        self.context['file_organization'] = self._extract_file_organization(content)
        self.context['testing_strategy'] = self._extract_testing_strategy(content)
        self.context['development_workflow'] = self._extract_workflow(content)
        
        # Extract Phase 5: Examples
        self.context['correct_example'] = self._extract_code_block(content, 'CORRECT')
        self.context['incorrect_example'] = self._extract_code_block(content, 'INCORRECT')
        
        print(f"   ✓ Extracted context for project: {self.context['project_name']}")
        
    def _extract_placeholder(self, content: str, pattern: str, default: str = '') -> str:
        """Extract placeholder value from interview record."""
        # Look for <PLACEHOLDER: pattern> or pattern in content
        regex = rf'<PLACEHOLDER:\s*{re.escape(pattern)}>'
        match = re.search(regex, content, re.IGNORECASE)
        if match:
            # Try to find the actual value after the placeholder
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if match.group(0) in line and i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line and not next_line.startswith('<'):
                        return next_line
        return default
    
    def _extract_services(self, content: str) -> List[Dict[str, str]]:
        """Extract services list from interview record."""
        services = []
        # Look for service definitions in Q2 response
        service_pattern = r'(\w+):\s*([^,]+?)(?:\s+on\s+port\s+(\d+))?'
        matches = re.finditer(service_pattern, content, re.IGNORECASE)
        for match in matches:
            services.append({
                'name': match.group(1),
                'tech_stack': match.group(2).strip(),
                'port': match.group(3) or '',
                'purpose': ''
            })
        return services if services else [{'name': 'app', 'tech_stack': 'unknown', 'port': '', 'purpose': ''}]
    
    def _extract_networking(self, content: str) -> Dict[str, str]:
        """Extract networking configuration."""
        return {
            'reverse_proxy': self._extract_placeholder(content, 'traefik | nginx | caddy | none', 'none'),
            'domain_pattern': self._extract_placeholder(content, 'domain_pattern', '*.local'),
            'port_strategy': self._extract_placeholder(
                content, 'traefik_labels | direct_ports | internal_only', 'direct_ports'
            )
        }
    
    def _extract_database_config(self, content: str) -> Dict[str, Any]:
        """Extract database configuration."""
        return {
            'type': self._extract_placeholder(content, 'supabase | postgresql | mongodb | mysql | none', 'none'),
            'self_hosted': 'self_hosted' in content.lower() or 'self-hosted' in content.lower(),
            'connection_pattern': self._extract_placeholder(
                content, 'container_name | external_url', 'container_name'
            )
        }
    
    def _extract_testing(self, content: str) -> Dict[str, str]:
        """Extract testing requirements."""
        return {
            'backend': self._extract_placeholder(content, 'pytest | jest | unittest | none', 'none'),
            'frontend': self._extract_placeholder(content, 'vitest | jest | cypress | none', 'none'),
            'e2e': self._extract_placeholder(content, 'playwright | cypress | none', 'none')
        }
    
    def _extract_list(self, content: str, list_name: str) -> List[str]:
        """Extract list items from interview record."""
        items = []
        pattern = rf'{list_name}.*?=.*?\[(.*?)\]'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            list_content = match.group(1)
            # Extract items from list
            item_pattern = r'<PLACEHOLDER:\s*"([^"]+)"\s*>'
            items = re.findall(item_pattern, list_content)
        return items
    
    def _extract_coding_standards(self, content: str) -> Dict[str, Any]:
        """Extract coding standards."""
        return {
            'backend': {
                'language': self._extract_placeholder(content, 'python | node | go | rust | java', 'python'),
                'linter': self._extract_placeholder(content, 'ruff | pylint | eslint', 'ruff'),
                'formatter': self._extract_placeholder(content, 'ruff | black | prettier', 'ruff'),
                'type_checker': self._extract_placeholder(content, 'mypy | typescript | none', 'mypy'),
                'line_length': int(self._extract_placeholder(content, 'line_length', '120')),
                'quote_style': self._extract_placeholder(content, 'double | single', 'double')
            },
            'frontend': {
                'framework': self._extract_placeholder(content, 'react | vue | angular | svelte', 'react'),
                'linter': self._extract_placeholder(content, 'eslint | biome', 'eslint'),
                'formatter': self._extract_placeholder(content, 'prettier | biome', 'prettier'),
                'type_checker': self._extract_placeholder(content, 'typescript | none', 'typescript'),
                'line_length': int(self._extract_placeholder(content, 'line_length', '120')),
                'quote_style': self._extract_placeholder(content, 'double | single', 'double')
            }
        }
    
    def _extract_file_organization(self, content: str) -> Dict[str, str]:
        """Extract file organization pattern."""
        return {
            'pattern': self._extract_placeholder(
                content, 'vertical_slice | feature_based | mvc | layered', 'feature_based'
            ),
            'structure': self._extract_placeholder(content, 'structure', 'Standard project structure')
        }
    
    def _extract_testing_strategy(self, content: str) -> Dict[str, str]:
        """Extract testing strategy."""
        return {
            'unit': self._extract_placeholder(content, 'unit', 'pytest'),
            'integration': self._extract_placeholder(content, 'integration', 'none'),
            'e2e': self._extract_placeholder(content, 'e2e', 'none')
        }
    
    def _extract_workflow(self, content: str) -> Dict[str, str]:
        """Extract development workflow."""
        return {
            'dependency_management': self._extract_placeholder(
                content, 'npm | pnpm | yarn | uv | poetry | pip', 'npm'
            ),
            'build_process': self._extract_placeholder(content, 'vite | webpack | tsc', 'vite'),
            'hot_reload': 'hot_reload' in content.lower() or 'hot reload' in content.lower()
        }
    
    def _extract_code_block(self, content: str, block_type: str) -> str:
        """Extract code block from interview record."""
        pattern = rf'{block_type}.*?```(?:.*?)?\n(.*?)```'
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        return match.group(1).strip() if match else ''
    
    def validate_context(self):
        """Validate that all critical context variables are present."""
        required = ['project_name', 'project_type', 'services']
        missing = [var for var in required if not self.context.get(var)]
        
        if missing:
            raise ValueError(
                f"Missing required context variables: {', '.join(missing)}\n"
                "Please complete the interview record with all required information."
            )
        
        print("   ✓ All critical context variables present")
    
    def load_templates(self) -> Dict[str, str]:
        """Load all template files from template directory."""
        templates = {}
        
        if not self.template_dir.exists():
            print(f"   ⚠ Template directory not found: {self.template_dir}")
            print("   → Creating minimal templates...")
            return self._create_minimal_templates()
        
        # Load all .template files
        for template_file in self.template_dir.rglob('*.template'):
            relative_path = template_file.relative_to(self.template_dir)
            templates[str(relative_path)] = template_file.read_text()
        
        print(f"   ✓ Loaded {len(templates)} template files")
        return templates
    
    def _create_minimal_templates(self) -> Dict[str, str]:
        """Create minimal templates if template directory doesn't exist."""
        return {
            '.cursorrules.template': self._get_default_cursorrules_template(),
            'rules/project-rules.mdc.template': self._get_default_project_rules_template(),
        }
    
    def _get_default_cursorrules_template(self) -> str:
        """Get default .cursorrules template."""
        return """# Cursor IDE Workspace Rules for <PLACEHOLDER: PROJECT_NAME>

**Project:** <PLACEHOLDER: PROJECT_NAME>
**Type:** <PLACEHOLDER: PROJECT_TYPE>
**Path:** <PLACEHOLDER: PROJECT_PATH>

## Project Context

<PLACEHOLDER: PROJECT_DESCRIPTION>

## Services

<PLACEHOLDER: SERVICES_LIST>

## Development Standards

<PLACEHOLDER: CODING_STANDARDS>

## Reference File Protection

**NEVER modify original reference files** from example configurations.
"""
    
    def _get_default_project_rules_template(self) -> str:
        """Get default project rules template."""
        return """---
alwaysApply: true
---
# Project Rules — <PLACEHOLDER: PROJECT_NAME>

This rules file applies to the repo root: `<PLACEHOLDER: PROJECT_PATH>`.

## Generated files location

**CRITICAL**: Store all generated artifacts here:
1. **Primary**: `<PLACEHOLDER: PROJECT_PATH>/.cursor/tmp/`
2. **Fallback**: `<PLACEHOLDER: PROJECT_PATH>/tmp/`

## Repo boundary safety

- **Do not modify files outside this repo** unless explicitly requested.
- **Respect the codebase structure** — main codebase lives at root.

## Reference file protection (CRITICAL)

**NEVER modify original reference files** from example configurations.
"""
    
    def generate_files(self, templates: Dict[str, str]):
        """Generate all workspace files from templates."""
        # Create .cursor directory structure
        cursor_dir = self.project_path / '.cursor'
        cursor_dir.mkdir(exist_ok=True)
        (cursor_dir / 'rules').mkdir(exist_ok=True)
        (cursor_dir / 'commands').mkdir(exist_ok=True)
        (cursor_dir / 'hooks').mkdir(exist_ok=True)
        (cursor_dir / 'tmp').mkdir(exist_ok=True)
        
        # Generate files from templates
        for template_path, template_content in templates.items():
            # Remove .template extension
            output_path = template_path.replace('.template', '')
            
            # Replace placeholders
            content = self.replace_placeholders(template_content)
            
            # Write file
            full_path = self.project_path / output_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content)
            self.generated_files.append(str(full_path.relative_to(self.project_path)))
        
        # Generate source_list.json
        self.generate_source_list()
        
        # Generate manifests
        self.generate_manifests()
        
        print(f"   ✓ Generated {len(self.generated_files)} files")
    
    def replace_placeholders(self, content: str) -> str:
        """Replace all placeholders in template content with context values."""
        # Replace simple placeholders
        replacements = {
            'PROJECT_NAME': self.context.get('project_name', 'Untitled Project'),
            'PROJECT_TYPE': self.context.get('project_type', 'fullstack'),
            'PROJECT_PATH': self.context.get('project_path', str(self.project_path)),
            'DATE': self.context.get('date', datetime.now().strftime('%Y-%m-%d')),
        }
        
        for key, value in replacements.items():
            content = content.replace(f'<PLACEHOLDER: {key}>', str(value))
        
        # Replace complex placeholders
        content = self._replace_services_list(content)
        content = self._replace_coding_standards(content)
        content = self._replace_networking_config(content)
        
        return content
    
    def _replace_services_list(self, content: str) -> str:
        """Replace services list placeholder."""
        if '<PLACEHOLDER: SERVICES_LIST>' not in content:
            return content
        
        services_text = []
        for service in self.context.get('services', []):
            services_text.append(
                f"- **{service['name']}** — {service['tech_stack']}"
                + (f" (Port {service['port']})" if service.get('port') else "")
            )
        
        return content.replace(
            '<PLACEHOLDER: SERVICES_LIST>',
            '\n'.join(services_text) if services_text else 'No services defined'
        )
    
    def _replace_coding_standards(self, content: str) -> str:
        """Replace coding standards placeholder."""
        if '<PLACEHOLDER: CODING_STANDARDS>' not in content:
            return content
        
        standards = self.context.get('coding_standards', {})
        backend = standards.get('backend', {})
        frontend = standards.get('frontend', {})
        
        text = []
        if backend:
            text.append("### Backend")
            text.append(f"- Language: {backend.get('language', 'python')}")
            text.append(f"- Linter: {backend.get('linter', 'ruff')}")
            text.append(f"- Formatter: {backend.get('formatter', 'ruff')}")
            text.append(f"- Type Checker: {backend.get('type_checker', 'mypy')}")
        
        if frontend:
            text.append("\n### Frontend")
            text.append(f"- Framework: {frontend.get('framework', 'react')}")
            text.append(f"- Linter: {frontend.get('linter', 'eslint')}")
            text.append(f"- Formatter: {frontend.get('formatter', 'prettier')}")
        
        return content.replace('<PLACEHOLDER: CODING_STANDARDS>', '\n'.join(text))
    
    def _replace_networking_config(self, content: str) -> str:
        """Replace networking configuration placeholder."""
        networking = self.context.get('networking', {})
        if '<PLACEHOLDER: NETWORKING_CONFIG>' in content:
            text = f"""
- Reverse Proxy: {networking.get('reverse_proxy', 'none')}
- Domain Pattern: {networking.get('domain_pattern', '*.local')}
- Port Strategy: {networking.get('port_strategy', 'direct_ports')}
"""
            content = content.replace('<PLACEHOLDER: NETWORKING_CONFIG>', text)
        return content
    
    def generate_source_list(self):
        """Generate source_list.json with documentation references."""
        source_list = {
            "version": "1.0.0",
            "generated_at": datetime.now().strftime('%Y-%m-%d'),
            "policy": {
                "evidence_required": True,
                "notes": [
                    "Entries in this file are authoritative sources used to ground templates and behaviors.",
                    "All non-trivial claims in generated kit docs should cite at least one source URL from this list."
                ]
            },
            "sources": self._get_documentation_sources()
        }
        
        source_list_path = self.project_path / 'source_list.json'
        source_list_path.write_text(json.dumps(source_list, indent=2))
        self.generated_files.append('source_list.json')
    
    def _get_documentation_sources(self) -> List[Dict[str, Any]]:
        """Get list of documentation sources based on project context."""
        sources = []
        
        # Always include Cursor documentation
        sources.extend(self._get_cursor_sources())
        
        # Add technology-specific sources
        if 'react' in self.context.get('frontend_stack', '').lower():
            sources.extend(self._get_react_sources())
        
        if 'python' in self.context.get('backend_stack', '').lower():
            sources.extend(self._get_python_sources())
        
        if 'docker' in self.context.get('deployment', '').lower():
            sources.extend(self._get_docker_sources())
        
        # Add other common sources
        sources.extend(self._get_common_sources())
        
        return sources
    
    def _get_cursor_sources(self) -> List[Dict[str, Any]]:
        """Get Cursor IDE documentation sources."""
        return [
            {
                "id": "cursor_rules",
                "title": "Cursor Docs: Rules",
                "url": "https://docs.cursor.com/context/rules",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "Project rules live in .cursor/rules as .mdc files.",
                    "Rules use frontmatter metadata (description, alwaysApply).",
                    "AGENTS.md is supported as a simple alternative."
                ],
                "use_when": [
                    "Generating .cursor/rules content",
                    "Deciding between AGENTS.md and rules files",
                    "Validating rule file format"
                ]
            },
            {
                "id": "cursor_commands",
                "title": "Cursor Docs: Commands",
                "url": "https://cursor.com/docs/agent/chat/commands",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "Project commands live in .cursor/commands as Markdown files.",
                    "Commands can be organized in subdirectories.",
                    "Commands support slash-command syntax."
                ],
                "use_when": [
                    "Generating slash commands for Cursor",
                    "Validating command placement and format"
                ]
            }
        ]
    
    def _get_react_sources(self) -> List[Dict[str, Any]]:
        """Get React documentation sources."""
        return [
            {
                "id": "react_docs",
                "title": "React Documentation",
                "url": "https://react.dev/",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "React 18+ uses functional components and hooks.",
                    "TanStack Query recommended for data fetching.",
                    "Vertical slice architecture recommended for features."
                ],
                "use_when": [
                    "Building React components",
                    "Setting up data fetching patterns",
                    "Organizing feature structure"
                ]
            }
        ]
    
    def _get_python_sources(self) -> List[Dict[str, Any]]:
        """Get Python documentation sources."""
        return [
            {
                "id": "python_docs",
                "title": "Python Documentation",
                "url": "https://docs.python.org/3/",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "Python 3.12+ recommended for modern projects.",
                    "Ruff is the recommended linter and formatter.",
                    "MyPy for type checking."
                ],
                "use_when": [
                    "Writing Python code",
                    "Setting up linting and formatting",
                    "Type checking configuration"
                ]
            }
        ]
    
    def _get_docker_sources(self) -> List[Dict[str, Any]]:
        """Get Docker documentation sources."""
        return [
            {
                "id": "docker_docs",
                "title": "Docker Documentation",
                "url": "https://docs.docker.com/",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "Docker Compose for multi-container applications.",
                    "Use container names for inter-service communication.",
                    "Health checks recommended for all services."
                ],
                "use_when": [
                    "Configuring Docker Compose",
                    "Setting up service communication",
                    "Implementing health checks"
                ]
            }
        ]
    
    def _get_common_sources(self) -> List[Dict[str, Any]]:
        """Get common documentation sources."""
        return [
            {
                "id": "claude_code_docs",
                "title": "Claude Code Documentation",
                "url": "https://claude.ai/code",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "Claude Code provides AI-powered code generation.",
                    "Follows similar patterns to Cursor IDE."
                ],
                "use_when": [
                    "Using Claude for code generation",
                    "Understanding AI coding assistant patterns"
                ]
            },
            {
                "id": "mcp_docs",
                "title": "Model Context Protocol Documentation",
                "url": "https://modelcontextprotocol.io/",
                "type": "official_docs",
                "trust_level": "high",
                "retrieved_at": datetime.now().strftime('%Y-%m-%d'),
                "key_facts": [
                    "MCP enables AI assistants to interact with external tools.",
                    "MCP servers expose tools via standardized protocol."
                ],
                "use_when": [
                    "Integrating MCP servers",
                    "Building MCP tools",
                    "Connecting AI assistants to external services"
                ]
            }
        ]
    
    def generate_manifests(self):
        """Generate manifest files for progressive context loading."""
        # Rules manifest
        rules_manifest = {
            "version": "1.0.0",
            "description": "Progressive context loading manifest for Cursor IDE rules",
            "rules": self._get_rules_manifest()
        }
        rules_manifest_path = self.project_path / '.cursor' / 'rules' / 'rules_manifest.json'
        rules_manifest_path.write_text(json.dumps(rules_manifest, indent=2))
        self.generated_files.append('.cursor/rules/rules_manifest.json')
        
        # Commands manifest
        commands_manifest = {
            "version": "1.0.0",
            "description": "Progressive context loading manifest for Cursor IDE commands",
            "commands": self._get_commands_manifest()
        }
        commands_manifest_path = self.project_path / '.cursor' / 'commands' / 'commands_manifest.json'
        commands_manifest_path.write_text(json.dumps(commands_manifest, indent=2))
        self.generated_files.append('.cursor/commands/commands_manifest.json')
        
        # Hooks manifest
        hooks_manifest = {
            "version": "1.0.0",
            "description": "Progressive context loading manifest for Cursor IDE hooks",
            "hooks": [],
            "note": "No hooks have been created yet."
        }
        hooks_manifest_path = self.project_path / '.cursor' / 'hooks' / 'hooks_manifest.json'
        hooks_manifest_path.write_text(json.dumps(hooks_manifest, indent=2))
        self.generated_files.append('.cursor/hooks/hooks_manifest.json')
    
    def _get_rules_manifest(self) -> List[Dict[str, Any]]:
        """Get rules manifest entries."""
        return [
            {
                "level": 1,
                "name": "Project Rules",
                "filename": "project-rules.mdc",
                "path": ".cursor/rules/project-rules.mdc",
                "alwaysApply": True,
                "description": "Core project-specific rules"
            }
        ]
    
    def _get_commands_manifest(self) -> List[Dict[str, Any]]:
        """Get commands manifest entries."""
        return []
    
    def validate_output(self):
        """Validate generated files."""
        issues = []
        
        # Check that .cursorrules exists
        cursorrules_path = self.project_path / '.cursorrules'
        if not cursorrules_path.exists():
            issues.append("Missing .cursorrules file")
        
        # Check that project-rules.mdc exists
        project_rules_path = self.project_path / '.cursor' / 'rules' / 'project-rules.mdc'
        if not project_rules_path.exists():
            issues.append("Missing .cursor/rules/project-rules.mdc file")
        
        if issues:
            print(f"   ⚠ Found {len(issues)} validation issues:")
            for issue in issues:
                print(f"      - {issue}")
        else:
            print("   ✓ All validation checks passed")
    
    def report_results(self):
        """Report setup results to user."""
        print("✅ Cursor workspace setup complete!\n")
        print("Generated files:")
        for file in self.generated_files:
            print(f"  - {file}")
        
        print("\nNext steps:")
        print("  1. Review generated .cursorrules")
        print("  2. Test commands in .cursor/commands/")
        print("  3. Validate rules match your project structure")
        print("  4. Commit to version control")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Setup Cursor IDE workspace from interview record and templates'
    )
    parser.add_argument(
        '--interview-record',
        required=True,
        help='Path to completed interview record markdown file'
    )
    parser.add_argument(
        '--project-path',
        required=True,
        help='Path to project root directory'
    )
    parser.add_argument(
        '--template-dir',
        default='.cursor/templates',
        help='Path to template directory (default: .cursor/templates)'
    )
    
    args = parser.parse_args()
    
    try:
        setup = CursorWorkspaceSetup(
            args.interview_record,
            args.project_path,
            args.template_dir
        )
        setup.run()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())

