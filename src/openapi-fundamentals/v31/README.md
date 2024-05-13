# OpenAPI Fundamentals

This course is designed to provide an overview of OpenAPI v3.1, from the bare essentials to extending OpenAPI and Special Interest Groups.

## Course Materials

- [Chapter 1 - Introducing OpenAPI](./chapter-1-introducing-openapi.md)
- [Chapter 2 - OpenAPI Basics](./chapter-2-openapi-basics.md)
- [Chapter 3 - Creating an OpenAPI Description](./chapter-3-creating-an-openapi-description.md)
- [Chapter 4 - Using an OpenAPI Description](./chapter-4-using-an-openapi-description.md)
- [Chapter 5 - Extending OpenAPI](./chapter-5-extending-openapi.md)

## Outline

The following sections provide an outline of the course modules.

### Chapter 1: Introducing OpenAPI

Understand the history of OpenAPI, its raison d’etre, and its place in the API economy.

#### Topics

- Introduction
  - Chapter Overview
  - Learning Objectives
- Introducing the API Economy
  - The role of APIs
  - APIs-as-Products
- Describing APIs
  - Describing Software Interfaces
  - What are API description languages?
  - What does an API description language solve for?
  - What API description languages are there?
- An Overview of OpenAPI
  - What is OpenAPI?
  - Other OpenAPI Initiative Specifications
- Knowledge Check

### Chapter 2: OpenAPI Basics

Understand the basic structure of an OpenAPI Description and how it reflects APIs published in the marketplace.

#### Topics

- Introduction
  - Chapter Overview
  - Learning Objectives
- HTTP, APIs and OpenAPI
  - The role of HTTP
  - Mapping OpenAPI to HTTP
    - Versions of OpenAPI
- High-Level Structure
  - Structure Overview
  - Providing Information
- Describing API Shape
  - URLs, Paths, and Methods
  - Model
- Describing Parameters, Requests and Responses
  - Providing Parameters
  - Creating Request and Response Objects
- Defining Reusable Objects
  - Objects That Can Be Reused
  - Example of Object Reuse
- Other Features
  - Grouping Operations using Tags
  - Describing Security Requirements
  - Supported Security Requirements
  - Security Requirement Example
  - Using Specification Extensions
- Course Scope
  - Features Not Covered
- Knowledge Check

### Chapter 3: Creating an OpenAPI Description

Create an OpenAPI Description using both code-first and design-first methodologies.

#### Topics

- Introduction
  - Chapter Overview
  - Learning Objectives
- Using Design-first
  - Why Design-first Works
  - Creating an OpenAPI Description in Swagger Editor
  - Adding an Info Object
  - Adding a Response Payload
  - Making a Response Reusable
  - Returning Consistent Error Payloads
  - Adding Tags to Operations
  - Adding Security Requirements
  - Other Information
  - Complete Example
- Using Code-first
  - Why Code-first Works
  - Code-first using Java and springdoc-openapi
  - Adding an Info Object
  - Adding a Response Payload
  - Adding Paths and Operations
  - Comparing Design-first
  - Code-first using Python and APIFlask
  - Adding an Info Object
  - Adding a Response Payload
  - Adding Paths and Operations
  - Code-first Tasks
  - Delete a Pet resource
  - Add a Tag
  - Add a Link
- Deciding on Design-first versus Code-first
  - What approach fits your needs?
  - Taking a Lifecycle View
- Knowledge Check

### Chapter 4: Using an OpenAPI Description

Use an OpenAPI Description with a range of tools that help you throughout the API lifecycle.

#### Topics

- Introduction
  - Chapter Overview
  - Learning Objectives
- Using an OpenAPI Description and the API lifecycle
  - The API Lifecycle
- Generating API Documentation
  - Use Case for Generating API Documentation
  - Example of Generating API Documentation
  - Task: Generate API documentation using Redoc
- Generating an API client
  - Use Case for Generating an API client
  - Example of Generating an API Client
  - Task: Generating an API Client using Kiota
- Applying Governance
  - Use Case for Applying Governance
  - Example of Applying Governance
  - Task: Add Governance Rules to a Spectral Ruleset
- Knowledge Check

### Chapter 5: Extending OpenAPI

Understand how OpenAPI is extended in the ecosystem through Specification Extensions and Special Interest Groups.

#### Topics

- Introduction
  - Chapter Overview
  - Learning Objectives
- Using Specification Extensions
  - What are Specification Extensions?
  - Example: UK Open Banking
  - Example: Redoc
  - Example: Azure API Management
  - Specification Extension Scope
- Overlay Specification
  - Updating OpenAPI Descriptions
  - Using the Overlay Specification
  - How Overlay Helps in Updating OpenAPI Descriptions
- Workflows Specification
  - Describing Sequences of API Calls
  - Describing a Workflow
  - Describing Steps
  - How Workflows Helps in Making Multiple API Calls
- Knowledge Check
