# Overlay Fundamentals v1.0.0

## Target Audience

- Anyone with working knowledge of the OpenAPI Specification.

## Chapter 1: Course Overview

> A candidate Course Overview section is not supplied in the course materials.
> Please develop your own, according to your learning objects.

- Define course objectives and scope.

  - Clarify expected outcomes for learners.

  - Set boundaries of what the course covers (Overlay v1.0.0, excludes OpenAPI
    Specification).

- Tailor emphasis based on audience (developers, product managers, architects).

  - Developers: Creation of update descriptions using Overlay, relationship to
    tooling.

  - Product managers: Use case for Overlay, enabler for automation.

  - Architects: Use case for Overlay, how Overlay fits into documentation
    pipeline.

## Chapter 2: Introducing Overlay

### Learning Objectives

On completion students should be able to:

- Explain how API economy has been shaped by use of API description languages.

- Describe the relationship between the Overlay Specification and Overlay
  Specification.

- Describe how Overlay supports creation of OpenAPI descriptions.

- Understand the concept of a Documentation Pipeline and of DocOps, where
  updates to documentation are automated through a standardized sequence of
  activities.

- Discuss how deterministic updates to OpenAPI descriptions drives efficiency,
  improves quality, and reduces cost.

### Requirements

- Introduce the concept of the API Economy:

  - Describe growth in number and usage of APIs.

  - Explain reason for popularity of API-based products and services.

- Introduce the need for well-described APIs and how API description languages
  benefit API consumers:

  - Describe why well-described APIs are essentially for bring products and
    services to market.

  - Discuss concept of API description language.

  - Describe history of languages and OpenAPI Specification.

- Describe approaches to creating OpenAPI descriptions:

  - Code-first, and annotation-based creation of OpenAPI description.

  - Design-first, and editor-based creation of OpenAPI descriptions.

- Explain why updating OpenAPI descriptions systematically is important:

  - Discuss stewardship of OpenAPI descriptions across an organization.

  - Explain how a given OpenAPI description can be "touched" by many
    stakeholders.

  - Describe why ensuring quality and accuracy of OpenAPI descriptions is
    important.

- Introduce Overlay:

  - Describe how the relationship between Overlay and OpenAPI.

- Describe a Documentation Pipeline in context of Overlay:

  - Introduce how automated updates can be achieved using Overlay.

  - Demonstrate how Overlay can be executed after the creation of an OpenAPI
    description.

  - Provide a pipeline-based view of this activity executed alongside other
    activities:

    - Spell check.

    - Proof read.

    - Style guide check.

- Discuss key benefits to Documentation Pipeline approach:

  - Determinism.

  - Efficiency.

  - Quality Improvement.

## Chapter 3: Overlay Basics

### Learning Objectives

On completion students should be able to:

- Explain the structure of an Overlay document.

- Explain how Overlay documents can be extended by reference.

- Describe how JSONPath is used to implement Overlay Actions.

- Describe the behaviors supported by an Overlay Action.

### Requirements

- Describe `overlay` field.

- Describe Info Object.

- Describe `extends` field:

  - Explain how `extends` references a specific OpenAPI document.

  - Introduce use cases for using `extends` (for example, governance for Overlay
    documents in a organizational API standards).

- Describe Action Object:

  - Purpose of Action Object.

  - How an Action Object locates the value of `target`.

    - Introduce JSONPath as corollary of XPath.

    - Describe evolution and implementation choices.

    - Walkthrough [RFC 9535](https://www.rfc-editor.org/rfc/rfc9535).

    - Show examples in context of an OpenAPI description document.

  - Behavior of an `update` Action:

    - Target object must be exist.

    - Content of `update` will be merged with existing object.

  - Behavior of `remove` Action.

## Chapter 4: Implementing an Overlay

### Learning Objectives

On completion students should be able to:

- Understand how Overlay documents can be created.

- Create an Overlay document using a reference OpenAPI description.

- Understand the tooling landscape and support for Overlay by tooling makers.

- Execute an Overlay using a tool.

- Understand the result of executing the Overlay.

### Requirements

- Show how an Overlay can be created.

  - Simple document, using schema validation through
    [Overlay JSON Schema](https://spec.openapis.org/overlay/1.0/schema/2024-10-22).

  - Introduce a vendor tool that allows an Overlay to be authored.

    - Trainer can choose most appropriate tool for the audience.

  - Describe practices for storing Overlay document (treated as code, stored in
    git repository, governed alongside OpenAPI documents).

  -

## Chapter 5: Extending Overlay

### Learning Objectives

On completion students should be able to:

- Describe how an Overlay document can be extended through Specification
  Extensions.

- Explain the role of tooling makers in supporting Overlay extensions.

### Requirements

- Describe the role of `x-` Specification Extension.

- Describe Specification Extensions in context of OpenAPI Initiative
  Specifications.

- Give practical examples of using Specification Extensions.

- Describe how tooling makers can leverage Specification Extensions to support
  deterministic behaviors in their toolsets.

  - Changing Overlay behaviors (merge vs. overwrite, create when target not
    found).

  - Providing dynamic behaviors in an Action Object (spelling and grammar
    functions, )
