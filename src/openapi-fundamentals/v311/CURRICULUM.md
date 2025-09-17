# OpenAPI Fundamentals v3.1.1

## Chapter 1: Course Overview

> A candidate Course Overview section is not supplied in the course materials. Please develop your own, according to your learning objects.

- Define course objectives and scope.

  - Clarify expected outcomes for learners (e.g., understand API economy, create and use OpenAPI descriptions, apply governance, extend OpenAPI).

  - Set boundaries of what the course covers (OpenAPI v3.1.1 only, not older Swagger versions in depth).

- Tailor emphasis based on audience (developers, product managers, architects).

  - Developers: focus on hands-on creation and tooling.

  - Product managers: focus on API lifecycle and product aspects.

  - Architects: focus on governance and organizational practices.

## Chapter 2: Introducing OpenAPI

**Learning Objectives**:

- Describe the API Economy.

- Explain why API description languages have become important.

- Discuss what OpenAPI is and why it is important.

### Section 2.1: The API Economy

- Explain the role of APIs in enabling modern digital services.

  - APIs allow distributed systems to communicate and scale.

  - Real-world example: Uber depends on external APIs for maps, messaging, and payments.

- Illustrate APIs-as-products and their lifecycle.

  - APIs are managed like products with roadmaps, backlogs, and product managers.

  - API lifecycles resemble product lifecycles, with stages from design to retirement.

- Describe the concept of the API economy and its business impact.

  - Businesses bring products to market via APIs, creating an “API economy.”

  - Industries adopt “open” models (e.g., open banking) where APIs are mandated.

### Section 2.2: Describing APIs

- Compare early description languages such as WSDL and IDL.

  - WSDL used in SOAP/SOA environments to generate clients.

  - IDLs tied to specific technology stacks, less flexible across styles.

- Show how REST and JSON shaped modern API practices.

  - HTTP became the default transport because it underpins the web.

  - JSON chosen for simplicity, broad support, and alignment with developer preferences.

- Explain the need for API description languages in HTTP/REST contexts.

  - REST did not enforce standard descriptions; discovery via hypermedia was insufficient.

  - Providers and consumers required concise, language-agnostic API descriptions.

### Section 2.3: API Description Languages

- Introduce RAML, API Blueprint, and Swagger.

  - All provided structured descriptions in JSON/YAML with Markdown for documentation.

- Explain the transition from Swagger to OpenAPI.

  - Swagger created by SmartBear and widely adopted.

  - Donated to the OpenAPI Initiative in 2015, forming the OpenAPI Specification.

- Highlight common features across description languages.

  - Specification of endpoints, methods, parameters, responses, and data structures.

### Section 2.4: What is OpenAPI?

- Define OpenAPI and its purpose.

  - Standard, machine- and human-readable way to describe HTTP APIs.

  - Enables reuse across the entire API lifecycle.

- Explain the role of the OpenAPI Initiative (OAI).

  - Oversees the specification and community adoption.

- Show how OpenAPI serves both human and machine audiences.

  - Humans: Markdown descriptions and structured layout for readability.

  - Machines: tooling support for client generation, validation, mocking, and more.

## Chapter 3: OpenAPI Basics

**Learning Objectives**:

- Explain the basics of the HTTP-based APIs.

- Describe how OpenAPI maps the features of HTTP-based APIs to its description language.

- Identify the features OpenAPI provides that reflect the needs of API consumers.

- Explain the basic structure of an OpenAPI description and why this structure provides an effective means of communication.

### Section 3.1: HTTP, APIs, and OpenAPI

- Review HTTP fundamentals: URLs, methods, status codes.

  - URLs as identifiers for resources.

  - Methods (GET, POST, PUT, DELETE) as operations.

  - Status codes as standardized outcomes of requests.

- Map HTTP features to OpenAPI objects (paths, operations, parameters, responses).

  - Paths Object = URLs.

  - Operation Object = HTTP methods.

  - Parameter Object = query, path, header, cookie parameters.

  - Request Body Object = payloads for POST/PUT.

  - Responses Object/Response Object = status codes and payloads.

### Section 3.2: Core Technologies in OpenAPI

- Demonstrate serialization with JSON and YAML.

  - OpenAPI documents can be written in either JSON or YAML.

- Use JSON Schema to define data models.

  - Schema Objects define properties of request/response payloads.

  - OpenAPI 3.1 supports JSON Schema Draft 2020-12.

- Apply Markdown for descriptive documentation.

  - CommonMark syntax enriches Info Object and descriptions.

### Section 3.3: Structure of an OpenAPI Document

- Identify the root OpenAPI Object.

  - Declares specification version and references other objects.

- Explain the role of the Info, Paths, and Components objects.

  - Info: metadata like title, version, description, license.

  - Paths: defines available operations.

  - Components: reusable objects such as schemas, responses, parameters.

### Section 3.4: Describing API Shape

- Define Paths, Path Items, and Operations.

  - Paths map URLs to Path Item Objects.

  - Path Items define supported HTTP methods.

  - Operations provide details: operationId, summary, tags.

- Explain parameter types (path, query, header, cookie).

  - Path parameters are placeholders in URLs (e.g., `/pets/{petId}`).

  - Query parameters modify behavior (e.g., filtering).

  - Header parameters for request metadata.

  - Cookies supported as parameter type.

- Describe request bodies and responses.

  - Request Body Object specifies payloads with media type and schema.

  - Response Object defines response payloads, status codes, headers.

- Use Schema Objects to model data.

  - Types: object, array, string, integer, etc.

  - Constraints: required, minLength, maxItems, pattern.

### Section 3.5: Versions of OpenAPI

- Trace evolution: Swagger 2.0 → OpenAPI 3.0 → OpenAPI 3.1.

  - Swagger 2.0 renamed to OpenAPI 2.0 in 2015.

  - OpenAPI 3.0 published in 2017 with major improvements.

  - OpenAPI 3.1.1 published in 2024 with JSON Schema alignment.

- Identify differences relevant to learners.

  - Object definitions may vary, but mapping to HTTP remains consistent.

## Chapter 4: Creating an OpenAPI Description

**Learning Objectives**:

- Describe the differences between design-first and code-first methodologies.

- Describe the design-first approach and the tools that can support it.

- Discuss the code-first methodology and examples of using code-first using supplied examples.

- Decide whether the design-first or code-first methodology best suits your needs, based on your role and what kind of organization you work for.

### Section 4.1: Design-first vs. Code-first Approaches

- Compare design-first and code-first methodologies.

  - Design-first: create the API description before implementation.

  - Code-first: generate description from implementation code.

- Identify pros, cons, and suitable contexts for each.

  - Design-first: enables collaboration and early feedback.

  - Code-first: integrates naturally into developer workflows.

### Section 4.2: Design-first with Swagger Editor

- Build a minimal OpenAPI description.

  - Define version, Info Object, and at least one Path/Operation.

- Add Info, Paths, Responses, and Schemas.

  - Info provides metadata.

  - Paths define endpoints.

  - Responses define return codes and payloads.

  - Schemas model response bodies.

- Create reusable components.

  - Move schema definitions into Components for reuse.

- Add Tags for navigation.

  - Tags group related operations, improving navigation in documentation.

- Define Security requirements.

  - Use Security Scheme Object (e.g., API keys) and Security Requirement.

- Configure Servers.

  - Server Object defines deployment URLs, descriptions, and variables.

### Section 4.3: Code-first Examples

- Generate an OpenAPI description using tools from at least two popular programming languages.

  - Annotate code with metadata to initialize the API description.

  - Decorate or annotate operations to add properties to each.

  - Generate description automatically at build time.

  - Output OpenAPI description document for use in other tools.

### Section 4.4: Best Practices

- Guide learners on choosing the right approach.

- Consider organizational maturity, team composition, and audience needs.

- Emphasize collaboration across product, architecture, and development teams.

- Ensure non-developers (e.g., product managers, architects) can review designs.

## Chapter 5: Using an OpenAPI Description

**Learning Objectives**:

- Discuss how OpenAPI supports activities of an API lifecycle

- Evaluate how OpenAPI is applied based on several use cases and examples

- Use OpenAPI in your organization's API lifecycle

### Section 5.1: OpenAPI in the API Lifecycle

- Explain stages of the API lifecycle: Design, Build, Test, Publish, Consume, Retire.

- Show how OpenAPI supports activities in each stage.

  - Design: define API shape.

  - Build/Test: validate and mock.

  - Publish: provide documentation and SDKs.

  - Consume: generate clients.

  - Retire: manage deprecation.

### Section 5.2: Documentation Generation

- Use OpenAPI descriptions to generate human-readable documentation.

  - Tools render descriptions into navigable docs.

- Demonstrate tools like Redoc.

  - Render Info, Paths, and Schemas into user-friendly format.

- Explain DocOps workflows.

  - Merge OpenAPI descriptions with other content for publication pipelines.

### Section 5.3: Client SDK and Code Generation

- Generate API clients with tools such as Kiota.

  - Process OpenAPI descriptions to create SDKs in multiple languages.

- Explain how providers and consumers use generated clients.

  - Providers: distribute SDKs to ease adoption.

  - Consumers: integrate APIs without hand-coding clients.

### Section 5.4: Applying Governance

- Apply design-time governance using tools like Spectral.

  - Lint OpenAPI descriptions against rulesets.

- Define rulesets and style guides for consistency.

  - Examples: require security for unsafe endpoints, enforce naming conventions.

### Section 5.5: Other Use Cases

- Mock APIs for testing.

  - Provide simulated responses before implementation is ready.

- Validate API designs against standards.

  - Ensure correctness, adherence to internal guidelines.

- Configure infrastructure such as API gateways.

  - Use OpenAPI descriptions to define gateway routing and security.

## Chapter 6: Extending OpenAPI

**Learning Objectives**:

- Explain how Specification Extensions are implemented, both conceptually and through exemplar.

- Discuss how Special Interest Groups (SIG) develop standards.

- Describe the purpose of the Overlay SIG and specification.

- Explain the purpose of the Workflows SIG and the Arazzo specification.

### Section 6.1: Specification Extensions

- Define `x-` extensions and their purpose.

  - Extend descriptions with custom properties.

- Show examples from UK Open Banking, Redoc, and Azure API Management.

  - `x-namespaced-enum` for error codes.

  - `x-logo` for custom branding in Redoc.

  - `x-ms-paths` to support query parameters in path definitions.

### Section 6.2: Overlay Specification

- Explain deterministic updates to OpenAPI descriptions.

- Overlays apply update/remove actions using JSONPath.

- Demonstrate JSONPath-based modifications.

- Target specific properties, update values, or remove parameters.

- Highlight use cases: translations, deployment configurations, SLAs.

  - Multi-language docs, environment-specific metadata, default responses.

### Section 6.3: Workflows & the Arazzo Specification

- Describe sequencing of API calls across multiple APIs.

- Define workflows to orchestrate API interactions.

- Define workflows and dependencies.

- Workflow Object specifies inputs, dependencies, and sequences.

- Show how OpenAPI and Workflow descriptions interlink.

- Show how workflow references source OpenAPI or Workflow documents.

### Section 6.4: Best Practices in Extending OpenAPI

- Instruct when to prefer core spec over extensions.

  - Use extensions only when core features are insufficient.

- Warn against overuse of proprietary extensions.

  - Multiple competing extensions degrade consumer experience.

- Stress usability and portability for consumers.

  - Ensure extensions can be safely ignored without breaking usage.

Do you want me to also create a **shortened “learning outcomes” version** (one line per section) for quick instructor reference, or keep only this detailed directive style?
