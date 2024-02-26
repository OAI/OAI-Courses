# OpenAPI Fundamentals

This course is designed to provide an overview of OpenAPI v3.1, from the bare essentials to extending OpenAPI and Special Interest Groups.

## Course Materials

- Module 1 - Introducing OpenAPI:
  - [Script](module-1-introducing-openapi.md)
  - [Slides](module-1-introducing-openapi.pptx)
- Module 2 - OpenAPI Basics:
  - [Script](module-2-openapi-basics.md)
  - [Slides](module-2-openapi-basics.pptx)
- Module 3 - Creating an OpenAPI document:
  - [Script](module-3-creating-an-openapi-document.md)
  - [Slides](module-3-creating-an-openapi-document.pptx)
- Module 4 - Using an OpenAPI document
- Module 5 - Extending OpenAPI

## Status

- Module 1
  - [x] Script drafted
  - [ ] Assets created
  - [ ] Community review complete
  - [ ] Final version published
- Module 2
  - [x] Script drafted
  - [ ] Assets created
  - [ ] Community review complete
  - [ ] Final version published
- Module 3
  - [x] Script drafted
  - [ ] Assets created
  - [ ] Community review complete
  - [ ] Final version published
- Module 4
  - [ ] Script drafted
  - [ ] Assets created
  - [ ] Community review complete
  - [ ] Final version published
- Module 5
  - [ ] Script drafted
  - [ ] Assets created
  - [ ] Community review complete
  - [ ] Final version published

## Outline

The following sections provide an outline of the course modules.

### Module 1: Introducing OpenAPI

Understand the history of OpenAPI, its raison d’etre, and its place in the API economy.

#### Topics

- The API Economy
- Describing APIs
- What do API specification languages do?
- The Role of OpenAPI

### Module 2: OpenAPI Basics

Understand the basic structure of an OpenAPI document and how it reflects APIs published in the marketplace.

#### Topics

- Versions of OpenAPI
- HTTP, APIs and OpenAPI
- Basic Structure
- Providing Information
- URLs, Paths, and Methods
- Providing Parameters
- Creating Request and Response Objects
- Defining Reusable Objects
- Describing Security Requirements
- Using Specification Extensions

### Module 3: Creating an OpenAPI document

Demonstrate the creation of OpenAPI using both Code-first and Design-first methodologies.

#### Topics

- How do you start? Code-first vs. Design-first
- Design-first:
  - Example in Swagger Editor
- Code-first approach:
  - Example in Python using Flask
  - Example in Java using Spring Boot
- What approach fits your needs?

### Module 4: Using an OpenAPI document

- What can you do with an OpenAPI document
  - Introduce the concept of an API lifecycle
  - Provide typical use cases
- Use case exploration
  - Importing an OpenAPI document in Postman
  - Generating a Python client code using [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/python)
  - Checking standards-compliance using Spectral

### Module 5: Extending OpenAPI

Show how OpenAPI underpins tools and extensions to the specification

#### Topics

- Introduce the (exceedingly common) concept of extending standards
- Using Specification Extensions
- Examples of implementing specification extensions (_use members who are vendors to show these in action_)
- Other specifications and Special Interest Groups (SIG) extend OpenAPI
- Examples of SIG work
  - [Overlays](https://github.com/OAI/Overlay-Specification)
  - [Workflows SIG](https://github.com/OAI/sig-workflows)
