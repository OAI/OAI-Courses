---
title: Overlay Fundamentals
description:
  Standard course curriculum for a course that introduces fundamentals of the
  Overlay Specification through a practical learning approach.
specification-version: v1.0.0
---

# Overlay Fundamentals

This document provides the curriculum for the Overlay Fundamentals course.

Overlay Fundamentals is designed to provide students with sufficient working
knowledge of the Overlay Specification to apply it in real world scenarios,
using Overlay as the cornerstone of an automated approach to updating OpenAPI
descriptions wherever deterministic updates need to be applied.

Providing defined curricula such as this document has two aims:

- Promoting standardization and consistency in how course materials for OpenAPI
  Initiative (OAI) Specifications are developed.

- Providing the basis of training programs certified by OAI as part of ongoing
  efforts to improve the value proposition for OAI members.

The ultimate goal is to provide the baseline for learning across the OAI
community, to ensure that the knowledge of our community grows alongside the
resources provided for learning, whomever provides those resources.

## Using This Document

This document provides the core curriculum for a Overlay Fundamentals course,
based on clear actionable learning objectives and requirements that should be
covered in course materials by course developers.

At this version of the document no means of assessing the implementation of the
learning objectives and requirements is provided. This will be remedied in
future versions, as the provision of a certification program is developed by
OAI.

## Course Audience

Overlay Fundamentals is expected to be a available to a wide range of
participants, and can include anyone with a working knowledge of the OpenAPI
Specification who can apply the materials described herein to real world
scenarios.

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

- Discuss key benefits to Documentation Pipeline approach:

  - Determinism.

  - Efficiency.

  - Quality Improvement.

- Describe a Documentation Pipeline in context of Overlay:

  - Introduce how automated updates can be achieved using Overlay.

  - Demonstrate how Overlay can be executed after the creation of an OpenAPI
    description.

  - Provide a pipeline-based view of this activity executed alongside other
    activities. Examples could include the following:

    - Insert standardized text to add, for example:

      - Marketing copy.

      - Legal disclaimer.

    - Added API security features, for example:

      - Update with Security Schemes defined at the API gateway.

      - Add to external documentation, for example security profiles or
        onboarding documentation.

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

  - Explain the use of the `version` field, and how that can be used to track
    changes to a given Overlay document over time.

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

      - Describe the evolution of the JSONPath through previous drafts.

      - Discuss implementations that have evolved around programming languages
        tooling (for example,
        [JSONPath Plus](https://www.npmjs.com/package/jsonpath-plus)).

      - Provide worked example of JSONPath expressions that are likely to be
        used in Overlay documents, including:

        - Basic Syntax.

        - Wildcards.

        - Filters.

        - Functions.

    - Show examples in context of an OpenAPI description document.

  - Behavior of an `update` Action:

    - Target object must be exist.

    - Content of `update` will be merged with existing object.

  - Behavior of `remove` Action.

    - Target object must be exist.

    - Object will be removed entirely from OpenAPI description.

    - What `remove` Action does not do without vendor support, for example:

      - Integrity checking (for example, broken References)

      - Recursively remove objects (for example, remove a "parent" Schema Object
        and all unused, referenced "children").

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

  - Show the development of a simple document, using schema validation through
    [Overlay JSON Schema](https://spec.openapis.org/overlay/1.0/schema/2024-10-22).

  - Introduce a vendor tool that allows an Overlay to be authored.

    - Trainer can choose most appropriate tool for the audience.

    - Tooling should place the Overlay in context of an existing, well-developed
      OpenAPI description document, with features that clearly indicate the role
      Overlay is playing in updating the document.

- Describe practices for storing Overlay document:

  - Overlay is treated as code.

  - Overlays are stored in git repository.

  - Governed alongside OpenAPI documents.

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

  - Providing dynamic behaviors in an Action Object, such as call outs to
    external functions like spelling and grammar tools.
