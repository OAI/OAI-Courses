# AGENTS.md

## Repository Overview
This is the **OpenAPI Initiative Courses** repository, which provides educational materials about OpenAPI. It's primarily a documentation and tutorial repository focused on teaching OpenAPI v3.1 fundamentals.

## Repository Type
- **Language**: Markdown-based documentation
- **Purpose**: Educational course materials for OpenAPI
- **Structure**: Course content organized in chapters with examples

## Key Directories

### `/src/`
- Contains source course materials in Markdown format
- Main course: `openapi-fundamentals/v31/`
- Organized by chapters (1-5) covering OpenAPI fundamentals

### `/build/`
- Contains built/compiled course materials
- Includes Word documents (.docx files) and example OpenAPI files
- Example OpenAPI specification: `openapi.yaml`

### `/src/openapi-fundamentals/v31/`
Core course content:
- `chapter-1-introducing-openapi.md` - Introduction to OpenAPI
- `chapter-2-openapi-basics.md` - Basic OpenAPI structure
- `chapter-3-creating-an-openapi-description.md` - Design-first and code-first approaches
- `chapter-4-using-an-openapi-description.md` - Tools and lifecycle
- `chapter-5-extending-openapi.md` - Extensions and special interest groups
- `chapter-3-examples/` and `chapter-4-examples/` - Practical examples

## Course Structure
The main course is "OpenAPI v3.1 Fundamentals" with 5 chapters:
1. **Introducing OpenAPI** - History, API economy, description languages
2. **OpenAPI Basics** - Structure, HTTP mapping, parameters, responses
3. **Creating OpenAPI Description** - Design-first vs code-first approaches
4. **Using OpenAPI Description** - Tools, documentation, clients, governance
5. **Extending OpenAPI** - Specification extensions, overlays, workflows

## File Types
- **Primary**: Markdown files (.md) for course content
- **Build outputs**: Word documents (.docx) - ignored in version control
- **Examples**: YAML files for OpenAPI specifications
- **Assets**: Images in `images/` directories

## Contributing Guidelines
- Fork repository for formal reviews
- Use GitHub Issues for bug reports
- Use GitHub Discussions for informal reviews and new content ideas
- Join OpenAPI Slack (#oai-courses channel) for discussions
- Add [sensiblewood](https://github.com/SensibleWood) as reviewer for PRs

## Build/Development Commands
*No specific build commands found - appears to be a documentation-only repository*

## Git Workflow
- Standard GitHub flow with forks and pull requests
- Use issue templates for bug reports and feature requests
- Community-driven review process through Slack coordination

## Special Notes
- Repository focuses on education rather than code
- Content is community-maintained
- Examples include both Java/Spring and Python/Flask implementations
- Uses real-world examples and practical exercises
