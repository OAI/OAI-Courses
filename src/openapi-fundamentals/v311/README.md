# OpenAPI Fundamentals

This course is designed to provide an overview of OpenAPI v3.1, from the bare essentials to extending OpenAPI, Special Interest Groups, and other specifications that are part of the OpenAPI Initiative.

## Course Materials

- [Chapter 1 - Course Overview](./chapter-1-course-overview.md)
- [Chapter 2 - Introducing OpenAPI](./chapter-2-introducing-openapi.md)
- [Chapter 3 - OpenAPI Basics](./chapter-3-openapi-basics.md)
- [Chapter 4 - Creating an OpenAPI Description](./chapter-4-creating-an-openapi-description.md)
- [Chapter 5 - Using an OpenAPI Description](./chapter-5-using-an-openapi-description.md)
- [Chapter 6 - Extending OpenAPI](./chapter-6-extending-openapi.md)

## Outline

The following sections provide an outline of the course modules.

### Chapter 1: Course Overview

Placeholder for a courser overview section, with the expectation any reusing these course materials will provide their own.

### Chapter 2: Introducing OpenAPI

Understand the history of OpenAPI, its raison d'etre, and its place in the API economy.

#### Topics

- [Introduction](./chapter-2-introducing-openapi.md#introduction)
  - [Chapter Overview](./chapter-2-introducing-openapi.md#chapter-overview)
  - [Learning Objectives](./chapter-2-introducing-openapi.md#learning-objectives)
- [Introducing the API Economy](./chapter-2-introducing-openapi.md#introducing-the-api-economy)
  - [The Role of APIs](./chapter-2-introducing-openapi.md#the-role-of-apis)
  - [APIs-as-Products](./chapter-2-introducing-openapi.md#apis-as-products)
- [Describing APIs](./chapter-2-introducing-openapi.md#describing-apis)
  - [Describing Software Interfaces](./chapter-2-introducing-openapi.md#describing-software-interfaces)
  - [What are API description languages?](./chapter-2-introducing-openapi.md#what-are-api-description-languages)
  - [What does an API description language solve for?](./chapter-2-introducing-openapi.md#what-does-an-api-description-language-solve-for)
  - [What API description languages exist?](./chapter-2-introducing-openapi.md#what-api-description-languages-exist)
- [An Overview of OpenAPI](./chapter-2-introducing-openapi.md#an-overview-of-openapi)
  - [What is OpenAPI?](./chapter-2-introducing-openapi.md#what-is-openapi)
  - [Other OpenAPI Initiative Specifications](./chapter-2-introducing-openapi.md#other-openapi-initiative-specifications)
- [Knowledge Check](./chapter-2-introducing-openapi.md#knowledge-check)

### Chapter 3: OpenAPI Basics

Understand the basic structure of an OpenAPI Description and how it reflects APIs published in the marketplace.

#### Topics

- [Introduction](./chapter-3-openapi-basics.md#introduction)
  - [Chapter Overview](./chapter-3-openapi-basics.md#chapter-overview)
  - [Learning Objectives](./chapter-3-openapi-basics.md#learning-objectives)
- [HTTP, APIs, and OpenAPI](./chapter-3-openapi-basics.md#http-apis-and-openapi)
  - [The Role of HTTP](./chapter-3-openapi-basics.md#the-role-of-http)
  - [Mapping OpenAPI to HTTP](./chapter-3-openapi-basics.md#mapping-openapi-to-http)
  - [Versions of OpenAPI](./chapter-3-openapi-basics.md#versions-of-openapi)
- [High-Level Structure](./chapter-3-openapi-basics.md#high-level-structure)
  - [Structure Overview](./chapter-3-openapi-basics.md#structure-overview)
  - [Providing Information through the Info Object](./chapter-3-openapi-basics.md#providing-information-through-the-info-object)
  - [Examples of the Info Object](./chapter-3-openapi-basics.md#examples-of-the-info-object)
- [Describing API Shape](./chapter-3-openapi-basics.md#describing-api-shape)
  - [URLs, Paths, and Methods](./chapter-3-openapi-basics.md#urls-paths-and-methods)
  - [Relationship Between Paths, Path Items and Operations](./chapter-3-openapi-basics.md#relationship-between-paths-path-items-and-operations)
- [Describing Parameters, Requests, and Responses](./chapter-3-openapi-basics.md#describing-parameters-requests-and-responses)
  - [Providing Parameters](./chapter-3-openapi-basics.md#providing-parameters)
  - [Using OpenAPI to Describe API Requests and Responses](./chapter-3-openapi-basics.md#using-openapi-to-describe-api-requests-and-responses)
  - [Representing Data Using a Schema Object](./chapter-3-openapi-basics.md#representing-data-using-a-schema-object)
  - [Creating a Response Object](./chapter-3-openapi-basics.md#creating-a-response-object)
- [Defining Reusable Objects](./chapter-3-openapi-basics.md#defining-reusable-objects)
  - [Objects That Can Be Reused](./chapter-3-openapi-basics.md#objects-that-can-be-reused)
  - [Example of Object Reuse](./chapter-3-openapi-basics.md#example-of-object-reuse)
- [Other Features](./chapter-3-openapi-basics.md#other-features)
  - [Grouping Operations using Tags](./chapter-3-openapi-basics.md#grouping-operations-using-tags)
  - [Describing Security Requirements](./chapter-3-openapi-basics.md#describing-security-requirements)
  - [Supported Security Requirements](./chapter-3-openapi-basics.md#supported-security-requirements)
  - [Security Requirement Example](./chapter-3-openapi-basics.md#security-requirement-example)
  - [Using Specification Extensions](./chapter-3-openapi-basics.md#using-specification-extensions)
- [Course Scope](./chapter-3-openapi-basics.md#course-scope)
  - [Features Not Covered Here](./chapter-3-openapi-basics.md#features-not-covered-here)
- [Knowledge Check](./chapter-3-openapi-basics.md#knowledge-check)

### Chapter 4: Creating an OpenAPI Description

Create an OpenAPI Description using both code-first and design-first methodologies.

#### Topics

- [Introduction](./chapter-4-creating-an-openapi-description.md#introduction)
  - [Chapter Overview](./chapter-4-creating-an-openapi-description.md#chapter-overview)
  - [Learning Objectives](./chapter-4-creating-an-openapi-description.md#learning-objectives)
- [Using Design-first](./chapter-4-creating-an-openapi-description.md#using-design-first)
  - [Why Design-first Works](./chapter-4-creating-an-openapi-description.md#why-design-first-works)
  - [Creating an OpenAPI Description in Swagger Editor](./chapter-4-creating-an-openapi-description.md#creating-an-openapi-description-in-swagger-editor)
  - [Adding an Info Object](./chapter-4-creating-an-openapi-description.md#adding-an-info-object)
  - [Adding a Response Payload](./chapter-4-creating-an-openapi-description.md#adding-a-response-payload)
  - [Making a Response Reusable](./chapter-4-creating-an-openapi-description.md#making-a-response-reusable)
  - [Returning Consistent Error Payloads](./chapter-4-creating-an-openapi-description.md#returning-consistent-error-payloads)
  - [Adding Tags to Operations](./chapter-4-creating-an-openapi-description.md#adding-tags-to-operations)
  - [Adding Security Requirements](./chapter-4-creating-an-openapi-description.md#adding-security-requirements)
  - [Other Information](./chapter-4-creating-an-openapi-description.md#other-information)
  - [Complete Example](./chapter-4-creating-an-openapi-description.md#complete-example)
- [Using Code-first](./chapter-4-creating-an-openapi-description.md#using-code-first)
  - [Why Code-first Works](./chapter-4-creating-an-openapi-description.md#why-code-first-works)
  - [Code-first Using Java and springdoc-openapi](./chapter-4-creating-an-openapi-description.md#code-first-using-java-and-springdoc-openapi)
  - [Comparing Design-first](./chapter-4-creating-an-openapi-description.md#comparing-design-first)
  - [Code-first using Python and APIFlask](./chapter-4-creating-an-openapi-description.md#code-first-using-python-and-apiflask)
  - [Code-first Tasks](./chapter-4-creating-an-openapi-description.md#code-first-tasks)
- [Deciding on Design-first versus Code-first](./chapter-4-creating-an-openapi-description.md#deciding-on-design-first-versus-code-first)
  - [Which Approach Fits Your Needs?](./chapter-4-creating-an-openapi-description.md#which-approach-fits-your-needs)
  - [Taking a Lifecycle View](./chapter-4-creating-an-openapi-description.md#taking-a-lifecycle-view)
- [Knowledge Check](./chapter-4-creating-an-openapi-description.md#knowledge-check)

### Chapter 5: Using an OpenAPI Description

Use an OpenAPI Description with a range of tools that help you throughout the API lifecycle.

#### Topics

- [Introduction](./chapter-5-using-an-openapi-description.md#introduction)
  - [Chapter Overview](./chapter-5-using-an-openapi-description.md#chapter-overview)
  - [Learning Objectives](./chapter-5-using-an-openapi-description.md#learning-objectives)
- [Using an OpenAPI Description and the API Lifecycle](./chapter-5-using-an-openapi-description.md#using-an-openapi-description-and-the-api-lifecycle)
  - [The API Lifecycle](./chapter-5-using-an-openapi-description.md#the-api-lifecycle)
- [Generating API Documentation](./chapter-5-using-an-openapi-description.md#generating-api-documentation)
  - [Use Case for Generating API Documentation](./chapter-5-using-an-openapi-description.md#use-case-for-generating-api-documentation)
  - [Example of Generating API Documentation](./chapter-5-using-an-openapi-description.md#example-of-generating-api-documentation)
  - [Task: Generate API Documentation Using Redoc](./chapter-5-using-an-openapi-description.md#task-generate-api-documentation-using-redoc)
- [Generating an API Client](./chapter-5-using-an-openapi-description.md#generating-an-api-client)
  - [Use Case for Generating an API Client](./chapter-5-using-an-openapi-description.md#use-case-for-generating-an-api-client)
  - [Example of Generating an API Client](./chapter-5-using-an-openapi-description.md#example-of-generating-an-api-client)
  - [Task: Generating an API Client using Kiota](./chapter-5-using-an-openapi-description.md#task-generating-an-api-client-using-kiota)
- [Applying Governance](./chapter-5-using-an-openapi-description.md#applying-governance)
  - [Use Case for Applying Governance](./chapter-5-using-an-openapi-description.md#use-case-for-applying-governance)
  - [Example of Applying Governance](./chapter-5-using-an-openapi-description.md#example-of-applying-governance)
  - [Task: Add Governance Rules to a Spectral Ruleset](./chapter-5-using-an-openapi-description.md#task-add-governance-rules-to-a-spectral-ruleset)
- [Knowledge Check](./chapter-5-using-an-openapi-description.md#knowledge-check)

### Chapter 6: Extending OpenAPI

Understand how OpenAPI is extended in the ecosystem through Specification Extensions and Special Interest Groups.

#### Topics

- [Introduction](./chapter-6-extending-openapi.md#introduction)
  - [Chapter Overview](./chapter-6-extending-openapi.md#chapter-overview)
  - [Learning Objectives](./chapter-6-extending-openapi.md#learning-objectives)
- [Using Specification Extensions](./chapter-6-extending-openapi.md#using-specification-extensions)
  - [What are Specification Extensions?](./chapter-6-extending-openapi.md#what-are-specification-extensions)
  - [Example: UK Open Banking](./chapter-6-extending-openapi.md#example-uk-open-banking)
  - [Example: Redoc](./chapter-6-extending-openapi.md#example-redoc)
  - [Example: Azure API Management](./chapter-6-extending-openapi.md#example-azure-api-management)
  - [Specification Extension Scope](./chapter-6-extending-openapi.md#specification-extension-scope)
- [Overlay Specification](./chapter-6-extending-openapi.md#overlay-specification)
  - [Updating OpenAPI Descriptions](./chapter-6-extending-openapi.md#updating-openapi-descriptions)
  - [Using the Overlay Specification](./chapter-6-extending-openapi.md#using-the-overlay-specification)
  - [How Overlay Helps in Updating OpenAPI Descriptions](./chapter-6-extending-openapi.md#how-overlay-helps-in-updating-openapi-descriptions)
- [Arazzo Specification (Workflows SIG)](./chapter-6-extending-openapi.md#arazzo-specification-workflows-sig)
  - [Describing Sequences of API Calls](./chapter-6-extending-openapi.md#describing-sequences-of-api-calls)
  - [Describing a Workflow](./chapter-6-extending-openapi.md#describing-a-workflow)
  - [Describing Steps](./chapter-6-extending-openapi.md#describing-steps)
  - [How Arazzo Helps in Making Multiple API Calls](./chapter-6-extending-openapi.md#how-arazzo-helps-in-making-multiple-api-calls)
- [Knowledge Check](./chapter-6-extending-openapi.md#knowledge-check)
