# SOP: Cursor IDE Workspace Setup for New Projects
## Standard Operating Procedure + Template Framework

**Version:** 1.0 Enterprise  
**Author:** Senior IT Architect & Product Developer  
**Date:** 2025-01-XX  
**Classification:** Internal Operations | Cursor IDE Configuration

---

## Executive Summary

This SOP provides a **structured, interview-driven framework** for setting up Cursor IDE workspace configuration for new projects. The framework uses a 5-phase interview process to extract project context, then automatically scaffolds a complete Cursor workspace with rules, commands, manifests, and documentation tailored to the specific project.

**Key Outcome:** Transform a new project into a fully-configured Cursor IDE workspace with 95%+ first-pass reliability, following zero-assumption principles and best practices.

---

## Table of Contents

1. [Framework Overview](#framework-overview)
2. [Five-Phase Interview Flow](#five-phase-interview-flow)
3. [Context Extraction Template](#context-extraction-template)
4. [Execution Script Usage](#execution-script-usage)
5. [Wrong vs. Correct Examples](#wrong-vs-correct-examples)
6. [Validation Checklist](#validation-checklist)
7. [Advanced Modifiers & Constraints](#advanced-modifiers--constraints)
8. [Real-World Integration Examples](#real-world-integration-examples)

---

## Framework Overview

### Why This Matters

Cursor IDE workspace setup succeeds when:
- ✅ Project architecture and technology stack are clearly understood
- ✅ Zero-assumption principles are applied (no guessing)
- ✅ Reference files are protected (never modify originals)
- ✅ Project-specific rules match actual codebase structure
- ✅ Commands align with actual development workflows
- ✅ Documentation references are accurate and complete

Cursor IDE workspace setup fails when:
- ❌ Assumptions are made about project structure
- ❌ Generic templates are applied without adaptation
- ❌ Reference files from examples are modified
- ❌ Rules don't match actual codebase patterns
- ❌ Commands reference non-existent services
- ❌ Documentation links are broken or irrelevant

This SOP bridges that gap through **structured discovery and automated scaffolding**.

### Core Principle: Interview-First, Scaffold-Second

The framework follows a **conversational, one-question-at-a-time methodology**:
1. Conduct 5-phase interview to extract project context
2. Document findings in Context Extraction Template
3. Run execution script with extracted context
4. Script scaffolds workspace from templates
5. Validate against checklist
6. Hand off to development team

---

## Five-Phase Interview Flow

### Phase 1: Project Classification (Q1)
**Goal:** Determine project type and primary technology stack.

**Question:**
> "What type of project is this — microservices application, monorepo, single-page application, infrastructure-as-code, data pipeline, API service, full-stack application, or something else?"

**Expected Responses & Variable Assignment:**
| Response | Variable | Next Filter |
|----------|----------|-------------|
| "Microservices application" | `project_type = "microservices"` | → Phase 2 (service-focused) |
| "Monorepo" | `project_type = "monorepo"` | → Phase 2 (multi-package) |
| "Single-page application" | `project_type = "spa"` | → Phase 2 (frontend-focused) |
| "Infrastructure-as-code" | `project_type = "iac"` | → Phase 2 (deployment-focused) |
| "Data pipeline" | `project_type = "data"` | → Phase 2 (processing-focused) |
| "API service" | `project_type = "api"` | → Phase 2 (backend-focused) |
| "Full-stack application" | `project_type = "fullstack"` | → Phase 2 (full-stack) |

**Adaptive Behavior:**
- If response is unclear, offer examples: "For example: React app with Node.js backend? Docker Compose stack? Terraform modules? Python data processing?"
- Save `project_type` as the first critical filter.

---

### Phase 2: Technology Stack & Architecture (Q2)
**Goal:** Extract technology stack, architecture patterns, and service structure.

**Question (adaptive to Phase 1 response):**

**If `project_type = "microservices"`:**
> "What services make up this application? List each service with its technology stack (e.g., 'archon-ui: React + TypeScript on port 3737', 'archon-server: FastAPI + Python on port 8181')."

**If `project_type = "monorepo"`:**
> "What packages or components are in this monorepo? List each with its purpose and technology stack."

**If `project_type = "spa"`:**
> "What frontend framework and build tool are you using? (e.g., React + Vite, Vue + Nuxt, Angular + CLI)"

**If `project_type = "iac"`:**
> "What infrastructure tools are you using? (e.g., Terraform, Pulumi, Docker Compose, Kubernetes)"

**If `project_type = "data"`:**
> "What data processing frameworks and storage systems are you using? (e.g., Apache Spark + PostgreSQL, Pandas + S3)"

**If `project_type = "api"`:**
> "What framework and language is the API built with? (e.g., FastAPI + Python, Express + Node.js, Spring Boot + Java)"

**If `project_type = "fullstack"`:**
> "What's the frontend and backend stack? List both with their technologies and ports."

**Expected Variables to Extract:**
```
services = [
  { name: "service-name", tech_stack: "framework + language", port: 8080, purpose: "description" }
]
frontend_stack = "framework + build_tool"
backend_stack = "framework + language"
database = "database_type + version"
deployment = "docker_compose | kubernetes | serverless | other"
architecture_pattern = "microservices | monolith | serverless | other"
```

**Adaptive Behavior:**
- Rephrase responses back to the user: "So you have [X] services, with [Y] as the frontend and [Z] as the backend?"
- Extract technology versions if mentioned.
- Flag any vague terms ("modern", "standard", "best practices") for clarification in Phase 3.

---

### Phase 3: Constraints & Requirements (Q3)
**Goal:** Identify non-negotiable constraints, deployment requirements, and integration points.

**Question:**
> "What are the critical constraints and requirements for this project? Consider: deployment environment (homelab, cloud, hybrid), networking requirements (Traefik, direct ports, internal only), database requirements (Supabase, PostgreSQL, MongoDB), secrets management, testing requirements, and any integration points with external services."

**Expected Variables to Extract:**
```
deployment_environment = "homelab | cloud | hybrid | local"
networking = {
  reverse_proxy: "traefik | nginx | caddy | none",
  domain_pattern: "*.1inks.org | *.local | custom",
  port_strategy: "traefik_labels | direct_ports | internal_only"
}
database = {
  type: "supabase | postgresql | mongodb | mysql | none",
  self_hosted: true | false,
  connection_pattern: "container_name | external_url"
}
secrets_management = ".env | docker_secrets | vault | other"
testing_requirements = {
  backend: "pytest | jest | unittest | none",
  frontend: "vitest | jest | cypress | none",
  e2e: "playwright | cypress | none"
}
integration_points = [
  { service: "name", type: "api | database | message_queue", connection: "details" }
]
hard_constraints = [
  "Constraint 1: exact requirement",
  "Constraint 2: exact requirement"
]
```

**Adaptive Behavior:**
- Listen for implicit constraints: "We're running on OrbStack" → `deployment_environment: homelab`
- Probe for edge cases: "What happens if the database is down? How do services discover each other?"
- Differentiate between hard constraints (break if violated) and soft constraints (optimize for).

---

### Phase 4: Development Workflow & Standards (Q4)
**Goal:** Uncover coding standards, file organization patterns, and development workflows.

**Conditional Questions (Choose Based on Project Type & Responses):**

**For Microservices/Full-Stack:**
> "What are your coding standards? (e.g., Python: Ruff + MyPy, TypeScript: ESLint + Biome, line length, quote style). How is the project organized? (e.g., vertical slice architecture, feature-based, MVC). What's your testing strategy?"

**For Monorepo:**
> "How are packages organized? What's the dependency management strategy? (e.g., npm workspaces, pnpm, yarn, uv). How do packages reference each other?"

**For Infrastructure:**
> "What's your deployment workflow? (e.g., manual scripts, CI/CD, GitOps). How do you manage environment-specific configurations?"

**Expected Variables to Extract:**
```
coding_standards = {
  backend: {
    language: "python | node | go | rust | java",
    linter: "ruff | pylint | eslint | golangci-lint",
    formatter: "ruff | black | prettier | gofmt",
    type_checker: "mypy | typescript | none",
    line_length: 120,
    quote_style: "double | single"
  },
  frontend: {
    framework: "react | vue | angular | svelte",
    linter: "eslint | biome",
    formatter: "prettier | biome",
    type_checker: "typescript | none",
    line_length: 120,
    quote_style: "double | single"
  }
}
file_organization = {
  pattern: "vertical_slice | feature_based | mvc | layered",
  structure: "description of directory layout"
}
testing_strategy = {
  unit: "framework",
  integration: "framework | none",
  e2e: "framework | none"
}
development_workflow = {
  dependency_management: "npm | pnpm | yarn | uv | poetry | pip",
  build_process: "vite | webpack | tsc | other",
  hot_reload: true | false
}
```

---

### Phase 5: Confirmation & Example Gathering (Q5)
**Goal:** Lock in understanding and gather concrete examples of correct vs. incorrect configuration.

**Question:**
> "Let me confirm: [Recap: project_type + tech_stack + constraints + standards]. Is that accurate? And can you share an example of what a CORRECT Cursor workspace setup looks like for this project vs. what an INCORRECT setup would be?"

**Expected Response:**
```
confirmation = "Yes" / "No, adjust [X]"
correct_example = "Specific example of desired .cursorrules or rule file"
incorrect_example = "Specific example of what NOT to do"
```

**Adaptive Behavior:**
- If "No", re-enter Phase 2, 3, or 4 with the adjustment.
- If "Yes", proceed to **Context Summary & Script Execution**.
- Use the examples to build guard clauses in generated rules.

---

## Context Extraction Template

Use this template to document your interview findings. Fill in as you progress through the five phases.

```markdown
# Cursor Workspace Setup Interview Record
**Date:** <PLACEHOLDER: DATE>
**Project Name:** <PLACEHOLDER: PROJECT_NAME>
**Project Path:** <PLACEHOLDER: /path/to/project>
**Stakeholder(s):** <PLACEHOLDER: NAMES>

---

## PHASE 1: Project Classification
**Q1 Response:**
<PLACEHOLDER: USER_RESPONSE_Q1>

**Extracted Variable:**
- `project_type` = <PLACEHOLDER: microservices | monorepo | spa | iac | data | api | fullstack>

---

## PHASE 2: Technology Stack & Architecture
**Q2 Response:**
<PLACEHOLDER: USER_RESPONSE_Q2>

**Extracted Variables:**
- `services` = [
    <PLACEHOLDER: { name: "service-name", tech_stack: "framework + language", port: 8080, purpose: "description" }>
  ]
- `frontend_stack` = <PLACEHOLDER: "framework + build_tool">
- `backend_stack` = <PLACEHOLDER: "framework + language">
- `database` = <PLACEHOLDER: "database_type + version">
- `deployment` = <PLACEHOLDER: docker_compose | kubernetes | serverless | other>
- `architecture_pattern` = <PLACEHOLDER: microservices | monolith | serverless | other>

---

## PHASE 3: Constraints & Requirements
**Q3 Response:**
<PLACEHOLDER: USER_RESPONSE_Q3>

**Extracted Variables:**
- `deployment_environment` = <PLACEHOLDER: homelab | cloud | hybrid | local>
- `networking` = {
    reverse_proxy: <PLACEHOLDER: traefik | nginx | caddy | none>,
    domain_pattern: <PLACEHOLDER: "*.1inks.org | *.local | custom">,
    port_strategy: <PLACEHOLDER: traefik_labels | direct_ports | internal_only>
  }
- `database` = {
    type: <PLACEHOLDER: supabase | postgresql | mongodb | mysql | none>,
    self_hosted: <PLACEHOLDER: true | false>,
    connection_pattern: <PLACEHOLDER: container_name | external_url>
  }
- `secrets_management` = <PLACEHOLDER: .env | docker_secrets | vault | other>
- `testing_requirements` = {
    backend: <PLACEHOLDER: pytest | jest | unittest | none>,
    frontend: <PLACEHOLDER: vitest | jest | cypress | none>,
    e2e: <PLACEHOLDER: playwright | cypress | none>
  }
- `integration_points` = [
    <PLACEHOLDER: { service: "name", type: "api | database | message_queue", connection: "details" }>
  ]
- `hard_constraints` = [
    <PLACEHOLDER: "Constraint 1: exact requirement">,
    <PLACEHOLDER: "Constraint 2: exact requirement">
  ]

---

## PHASE 4: Development Workflow & Standards
**Q4 Response:**
<PLACEHOLDER: USER_RESPONSE_Q4>

**Extracted Variables:**
- `coding_standards` = {
    backend: {
      language: <PLACEHOLDER: python | node | go | rust | java>,
      linter: <PLACEHOLDER: ruff | pylint | eslint | golangci-lint>,
      formatter: <PLACEHOLDER: ruff | black | prettier | gofmt>,
      type_checker: <PLACEHOLDER: mypy | typescript | none>,
      line_length: <PLACEHOLDER: 120>,
      quote_style: <PLACEHOLDER: double | single>
    },
    frontend: {
      framework: <PLACEHOLDER: react | vue | angular | svelte>,
      linter: <PLACEHOLDER: eslint | biome>,
      formatter: <PLACEHOLDER: prettier | biome>,
      type_checker: <PLACEHOLDER: typescript | none>,
      line_length: <PLACEHOLDER: 120>,
      quote_style: <PLACEHOLDER: double | single>
    }
  }
- `file_organization` = {
    pattern: <PLACEHOLDER: vertical_slice | feature_based | mvc | layered>,
    structure: <PLACEHOLDER: "description of directory layout">
  }
- `testing_strategy` = {
    unit: <PLACEHOLDER: "framework">,
    integration: <PLACEHOLDER: "framework | none">,
    e2e: <PLACEHOLDER: "framework | none">
  }
- `development_workflow` = {
    dependency_management: <PLACEHOLDER: npm | pnpm | yarn | uv | poetry | pip>,
    build_process: <PLACEHOLDER: vite | webpack | tsc | other>,
    hot_reload: <PLACEHOLDER: true | false>
  }

---

## PHASE 5: Confirmation & Examples
**Q5 Response:**
<PLACEHOLDER: USER_RESPONSE_Q5>

**Confirmation:** <PLACEHOLDER: YES | NO - Adjust: ...>

**Correct Example:**
\`\`\`
<PLACEHOLDER: EXAMPLE_OF_DESIRED_CURSOR_CONFIGURATION>
\`\`\`

**Incorrect Example:**
\`\`\`
<PLACEHOLDER: EXAMPLE_OF_UNDESIRED_CURSOR_CONFIGURATION>
\`\`\`

---

## SYNTHESIS: Context Summary
> **Project Type:** <PLACEHOLDER: project_type>  
> **Primary Stack:** <PLACEHOLDER: frontend_stack + backend_stack>  
> **Deployment:** <PLACEHOLDER: deployment_environment + deployment>  
> **Key Constraint:** <PLACEHOLDER: Most critical hard_constraint>  
> **Success = :** <PLACEHOLDER: Workspace fully configured and validated>

---
```

---

## Execution Script Usage

### Prerequisites

1. Python 3.12+ installed
2. Interview record completed (Context Extraction Template filled)
3. Project root directory identified
4. Reference templates available (included with script)

### Running the Script

```bash
# Navigate to project root
cd /path/to/<PLACEHOLDER: PROJECT_NAME>

# Run the execution script
python3 setup_cursor_workspace.py \
  --interview-record interview-record.md \
  --project-path . \
  --template-dir .cursor/templates
```

### Script Behavior

1. **Parse Interview Record**: Extracts all variables from completed template
2. **Validate Context**: Checks for missing critical variables
3. **Load Templates**: Reads template files from template directory
4. **Replace Placeholders**: Substitutes `<PLACEHOLDER: ...>` with extracted values
5. **Generate Files**: Creates directory structure and files:
   - `.cursorrules` (main workspace rules)
   - `.cursor/rules/*.mdc` (project-specific rules)
   - `.cursor/commands/**/*.md` (development commands)
   - `.cursor/AGENTS.md` (agent configuration)
   - `.cursor/rules/rules_manifest.json` (progressive context loading)
   - `.cursor/commands/commands_manifest.json` (commands manifest)
   - `.cursor/hooks/hooks_manifest.json` (hooks manifest)
   - `source_list.json` (local knowledge base)
6. **Validate Output**: Runs validation checks
7. **Report Results**: Displays summary and next steps

### Script Output

```
✅ Cursor workspace setup complete!

Generated files:
  - .cursorrules
  - .cursor/rules/project-rules.mdc
  - .cursor/rules/docker-homelab.mdc
  - .cursor/rules/<PLACEHOLDER: tech>-backend.mdc
  - .cursor/rules/<PLACEHOLDER: tech>-frontend.mdc
  - .cursor/commands/docker/start-services.md
  - .cursor/commands/testing/run-backend-tests.md
  - .cursor/commands/testing/run-frontend-tests.md
  - .cursor/AGENTS.md
  - source_list.json

Next steps:
  1. Review generated .cursorrules
  2. Test commands: .cursor/commands/docker/start-services.md
  3. Validate rules match your project structure
  4. Commit to version control
```

---

## Wrong vs. Correct Examples

### Example 1: Microservices Application

#### ❌ WRONG Interview Outcome

**Q1 Response:** "It's a web application."  
**Q2 Response:** "React frontend and Python backend."  
**Q3 Response:** "Docker Compose."  
**Q4 Response:** "Standard practices."  
**Q5 Response:** [No examples provided]

**Why This Fails:**
- No clarity on service structure (how many services? ports? names?)
- No constraints defined (Traefik? direct ports? domain pattern?)
- No coding standards specified (which linter? line length?)
- No example of correct configuration
- Script generates generic templates that don't match architecture

#### ✅ CORRECT Interview Outcome

**Q1 Response:** "Microservices application — specifically, Archon knowledge management system with 5 services."  
**Q2 Response:** 
- "archon-ui: React + TypeScript + Vite on port 3737"
- "archon-server: FastAPI + Python 3.12 on port 8181"
- "archon-mcp: MCP protocol server on port 8051"
- "archon-agents: PydanticAI agents on port 8052"
- "Supabase: Self-hosted PostgreSQL + PGVector"

**Q3 Response:**
- Hard Constraint: "Must use Traefik reverse proxy, no direct port exposure"
- Hard Constraint: "Domain pattern: *.1inks.org with archon- prefix for Supabase services"
- Hard Constraint: "Container names must use archon- prefix"
- Edge Case: "Services communicate via container names, not localhost"

**Q4 Response:** 
- "Python: Ruff linting, MyPy type checking, 120 char lines, double quotes"
- "TypeScript: Biome for /src/features/, ESLint for legacy, strict mode"
- "Testing: Pytest for backend, Vitest for frontend"
- "File organization: Vertical slice architecture in /features"

**Q5 Response:**
- Correct: `.cursorrules` with specific service ports, Traefik labels documented, three-domain Supabase pattern, runtime verification rules
- Incorrect: Generic `.cursorrules` with localhost references, no Traefik documentation, missing container name verification

**Why This Works:**
- Clear service structure, constraints, and standards
- Script generates production-ready configuration
- Edge cases are anticipated
- Examples prevent common mistakes

---

### Example 2: Monorepo Setup

#### ❌ WRONG Interview Outcome

**Q1 Response:** "It's a monorepo."  
**Q2 Response:** "Multiple packages."  
**Q3 Response:** "npm workspaces."  
**Q4 Response:** "TypeScript everywhere."  
**Q5 Response:** [No examples]

**Why This Fails:**
- No clarity on package structure (what packages? dependencies?)
- No constraints on package organization
- No standards for inter-package references
- AI generates generic monorepo config that doesn't match structure

#### ✅ CORRECT Interview Outcome

**Q1 Response:** "Monorepo — specifically, a design system with 3 packages: components, tokens, and utils."  
**Q2 Response:**
- "packages/components: React + TypeScript, exports UI components"
- "packages/tokens: JSON + TypeScript, exports design tokens"
- "packages/utils: TypeScript, exports utility functions"
- "Root: Vite + TypeScript for documentation site"

**Q3 Response:**
- Hard Constraint: "Packages use pnpm workspaces, no npm or yarn"
- Hard Constraint: "Internal packages use workspace: protocol, no file: references"
- Hard Constraint: "All packages must be published to npm registry"

**Q4 Response:**
- "TypeScript strict mode for all packages"
- "ESLint with shared config at root"
- "Prettier with shared config"
- "Vitest for testing all packages"

**Q5 Response:**
- Correct: `.cursorrules` with pnpm workspace commands, package-specific rules, inter-package dependency patterns
- Incorrect: Generic `.cursorrules` with npm commands, no workspace awareness, file: protocol references

**Why This Works:**
- Clear package structure and dependencies
- Constraint on package manager prevents conflicts
- Script generates workspace-aware configuration
- Examples prevent common monorepo mistakes

---

## Validation Checklist

Before considering the workspace setup complete, verify:

- [ ] **All 5 Phases Completed:** Interview record is filled out completely
- [ ] **Variables Extracted:** All critical variables are documented (project_type, services, constraints, standards)
- [ ] **Context Summary Written:** 2-3 sentence recap that script can use
- [ ] **Correct & Incorrect Examples Provided:** AI has guard rails and knows what NOT to do
- [ ] **Constraints are Explicit:** No vague terms like "standard", "modern", "best practices" (define in measurable units)
- [ ] **Edge Cases Listed:** At least 2-3 failure scenarios with handling strategy
- [ ] **Integration Points Clear:** Script knows where services connect and with what format
- [ ] **Success Metrics Defined:** Can validate output against these
- [ ] **Output Format Specified:** Script knows exact file types, structure, and style
- [ ] **Reference Files Protected:** Rules specify never modify original reference files
- [ ] **Zero-Assumption Principles Applied:** All recommendations cite sources
- [ ] **Stakeholders Aware:** Approval gate identified; no surprises post-generation

---

## Advanced Modifiers & Constraints

### Constraint Prioritization Matrix

Use this to communicate nuance about constraint importance:

| Constraint | Type | Must Have? | Impact if Broken | Example |
|------------|------|-----------|-----------------|---------|
| "Traefik routing only" | Hard | YES | Services unreachable | Homelab deployment |
| "No direct port exposure" | Hard | YES | Security/compliance breach | Production app |
| "120 char line length" | Soft | NO | Code formatting inconsistency | Python backend |
| "TypeScript strict mode" | Hard | YES | Type safety lost | Frontend app |
| "Container name verification" | Hard | YES | Wrong service accessed | Multi-project homelab |
| "Reference files read-only" | Hard | YES | Original examples corrupted | Template usage |

---

## Real-World Integration Examples

### Example: Handoff to Execution Script

**File Structure:**
```
project-root/
├── interview-record.md              [← Filled Interview Record]
├── setup_cursor_workspace.py        [← Execution Script]
├── .cursor/
│   ├── templates/                   [← Template Files]
│   │   ├── .cursorrules.template
│   │   ├── rules/
│   │   │   ├── project-rules.mdc.template
│   │   │   ├── docker-homelab.mdc.template
│   │   │   └── ...
│   │   └── commands/
│   │       └── ...
│   └── [Generated files after script run]
└── source_list.json                 [← Generated Knowledge Base]
```

**Run Script:**
```bash
python3 setup_cursor_workspace.py \
  --interview-record interview-record.md \
  --project-path . \
  --template-dir .cursor/templates
```

**Result:**
- Complete `.cursor/` directory structure
- All rules with placeholders replaced
- All commands tailored to project
- `source_list.json` with relevant documentation
- Validation report

---

## Quick Start Checklist

**To use this SOP for your next project:**

1. ✅ Copy the **Context Extraction Template** to `interview-record.md`
2. ✅ Schedule a 30-min interview with the stakeholder
3. ✅ Work through **Phase 1 → Phase 5** (one question at a time)
4. ✅ Fill in the **Interview Record** as you go
5. ✅ Gather **2-3 correct and incorrect examples** from the stakeholder
6. ✅ Run the **Execution Script** with completed interview record
7. ✅ Validate against the **Validation Checklist**
8. ✅ Review generated files and adjust if needed
9. ✅ Commit to version control
10. ✅ Celebrate — your Cursor workspace is production-ready! 🚀

---

## Appendix: Quick Reference Cards

### Card 1: The Five Questions (Print & Keep Handy)

```
┌─────────────────────────────────────────────────────────────┐
│ THE FIVE-PHASE INTERVIEW FRAMEWORK                          │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│ Q1: Project Classification                                   │
│     "What type of project — [microservices, monorepo, spa,   │
│      iac, data, api, fullstack, or something else]?"        │
│                                                               │
│ Q2: Technology Stack & Architecture (Adaptive)              │
│     "What services/packages? What tech stack? What ports?" │
│                                                               │
│ Q3: Constraints & Requirements                              │
│     "What are critical constraints? Deployment? Networking? │
│      Database? Testing?"                                     │
│                                                               │
│ Q4: Development Workflow & Standards (Adaptive)              │
│     "What coding standards? File organization? Testing?"   │
│                                                               │
│ Q5: Confirmation & Examples                                  │
│     "Is my understanding correct? Show me RIGHT vs. WRONG." │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### Card 2: Variable Extraction Checklist

```
┌─────────────────────────────────────────────────────────────┐
│ CRITICAL VARIABLES TO EXTRACT                               │
├─────────────────────────────────────────────────────────────┤
│ [ ] project_type (microservices|monorepo|spa|iac|...)      │
│ [ ] services (name, tech_stack, port, purpose)              │
│ [ ] frontend_stack (framework + build_tool)                 │
│ [ ] backend_stack (framework + language)                    │
│ [ ] database (type, self_hosted, connection_pattern)       │
│ [ ] deployment_environment (homelab|cloud|hybrid|local)     │
│ [ ] networking (reverse_proxy, domain_pattern, port_strategy)│
│ [ ] coding_standards (linter, formatter, type_checker, ...) │
│ [ ] file_organization (pattern, structure)                  │
│ [ ] testing_strategy (unit, integration, e2e)               │
│ [ ] hard_constraints (cannot violate)                       │
│ [ ] correct_example (desired configuration)                 │
│ [ ] incorrect_example (what NOT to do)                      │
│                                                               │
│ If ANY variable is missing or vague → loop back to relevant │
│ phase and re-interview.                                      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

---

**End of SOP Document**

---

## Footer & Metadata

| Attribute | Value |
|-----------|-------|
| **Audience** | Senior architects, lead engineers, DevOps teams, project managers |
| **Use Case** | Setting up Cursor IDE workspace for new projects |
| **Tools Supported** | Cursor IDE, Python 3.12+, execution script |
| **Expected ROI** | 95%+ first-pass workspace setup success; 80% reduction in manual configuration time |
| **Maintenance Cycle** | Quarterly review; update on new pattern discovery |
| **License** | Internal Use — Enterprise Operations |

---

*This SOP is designed for teams building production systems where reliability and predictability are non-negotiable. Use it. Refine it. Share it. Scale with confidence.*

