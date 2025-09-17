# Extending OpenAPI

## Introduction

### Chapter Overview

The OpenAPI Specification is the principal standard delivered by the OpenAPI Initiative (OAI). It is not, however, the only specification that falls under the OAI umbrella, and there are several other OAI specifications that provide additional functionality to both the API community and the tooling makers that support it.

The OpenAPI Specification also supports a standardized extension mechanism, which is commonly used by tooling makers to support specific functionality for the tools they provide. Using Specification Extensions provides a structured and deterministic way to deliver the description they need to support their communities.

### Learning Objectives

By the end of this chapter you should be able to:

- Explain how Specification Extensions are implemented, both conceptually and through exemplar.

- Discuss how Special Interest Groups (SIG) develop standards.

- Describe the purpose of the Overlay SIG and specification.

- Explain the purpose of the Workflows SIG and the Arazzo specification.

## Using Specification Extensions

### What are Specification Extensions?

[Specification Extensions](https://spec.openapis.org/oas/v3.1.1.html#specification-extensions) are a feature of the OpenAPI specification that we have yet to cover in our earlier chapters. They provide a structured approach to extending OpenAPI descriptions and can be used in virtually any object. They allow API providers and tooling makers to add customizations that complement their use cases or products.

Extension property names are always prefixed with x-. This prefix indicates that they are not properties of the core OpenAPI Specification and, therefore, should either be ignored or consumed based on a tooling maker or API consumer's understanding of what they represent. It is always safe to ignore extensions.

Other guidance in the OpenAPI Specification is relatively light as the use of this object is left to implementers. The main benefit is to allow OpenAPI to be tailored to specific use cases and scenarios using a deterministic approach.

### Example: UK Open Banking

The easiest way of showing the utility of Specification Extensions is by example. Take, for example, the UK open banking [Payment Initiation OpenAPI description](https://raw.githubusercontent.com/OpenBankingUK/read-write-api-specs/master/dist/openapi/payment-initiation-openapi.yaml). The specification implements an extension entitled **x-namespaced-enum** which defines a list of values that apply to a given string-based property and are set by the standards body that created the document.

The example below shows some of the possible values of the property **ErrorCode** as specified in the standards:

```yaml
OBError1:
  type: "object"
  additionalProperties: false
  properties:
    ErrorCode:
      description: "Low level textual error code, e.g., UK.OBIE.Field.Missing"
      type: "string"
      x-namespaced-enum:
        - "UK.OBIE.Field.Expected"
        - "UK.OBIE.Field.Invalid"
        - "UK.OBIE.Field.InvalidDate"
        - "UK.OBIE.Field.Missing"
        ...
```

A better approach might appear to be to use an `enum` property. However, the reason for using a Specification Extension is twofold:

- The standards body wanted to try to avoid breaking changes by specifying this list in an extension, which "could" be ignored when creating new versions.

- The list is guidance for banks to implement and therefore was better served as a Specification Extension rather than an **enum**.

This solution allowed the list to be published and to be machine-readable, but without resulting in the brittleness that the standards body was trying to avoid. You could argue that this is just semantics and changes to this list are a breaking change anyway, but it ensures that changes were isolated away from the enum value and therefore not disruptive when consumed by tooling.

### Example: Redoc

The Redoc example shows how providing additional information to API consumers can be facilitated. Tooling makers can follow a similar path in providing affordances for API providers to implement additional properties. A simple example is how Redoc [provides](https://github.com/Redocly/redoc?tab=readme-ov-file#openapi-specification-extensions) the means to customize their API documentation based solely on the content of Specification Extension properties, for example, to swap out the Redoc logo:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
  x-logo: https://www.openapis.org/wp-content/uploads/sites/3/2018/02/OpenAPI_Logo_Pantone-1.png
```

### Example: Azure API Management

One final example of using Specification Extensions is to help configure API-related infrastructure. Tooling makers often use Extensions to allow API providers who use their tooling to provide additional configuration data.

The example below shows how this is supported in Azure API Management. Microsoft provides the extension [`x-ms-paths`](https://github.com/Azure/autorest/tree/main/docs/extensions#x-ms-paths) to allow Path Item identifiers to include query parameters in order to complement how their API Management product can be configured to serve traffic:

```yaml
# Regular Path Item
paths:
  "/pets":
    get: ...

# Extended Path Item, with support for query parameters
x-ms-paths:
  "/pets?color={color}":
    get:
      parameters: ...
```

Note that this approach is opinionated - in that it reflects what one organization thinks about this property - and serves the purposes of Microsoft and their product consumers.

There is, however, a point to make here. In the same vein as Microsoft, you need to look hard at how you use Specification Extensions and how they can be leveraged to serve the needs of your API or tools. It goes without saying that wherever possible you should use the core OpenAPI Specification first and then leverage Extensions only where strictly necessary. Remember that your API or tools are unlikely to be the only ones your customer or API consumer uses. Making them deal with many different Extensions - unless there is a genuine need - is likely to degrade their experiences with your tools or APIs.

### Specification Extension Scope

Specification Extensions provide the opportunity to "fill in the gaps" in the OpenAPI Specification where special cases or specific requirements dictate.

There comes a point, however, where the OpenAPI specification cannot do it all on its own. This is where other specifications help provide an approach or standards that fulfill a specific use case or address a given industry vertical. Some of these specifications coalesce around an OAI Special Interest Group, or SIG, with a good number that are actively developing specifications.

We'll look at two SIGs, namely Overlay and Workflows.

## Overlay Specification

### Updating OpenAPI Descriptions

In the Specification Extensions section, we discussed how permissive the OpenAPI Specification is. However, this openness is something of a [curate's egg](https://en.wikipedia.org/wiki/Curate's_egg). It can be difficult to "know" how to process a given OpenAPI description deterministically or to apply updates later in the API lifecycle after the core OpenAPI description has been created. You may also _proactively_ decide to update your OpenAPI description later in the API lifecycle. Updating an OpenAPI description throughout your API lifecycle is common, as the source of truth for an aspect of the description may not be aligned with the software development lifecycle. The team in charge of making updates may also work at a different cadence to API designers or developers, with technical writers adding to a given OpenAPI description late in the API lifecycle.

Take, for example, the following examples of when an OpenAPI description may need to be updated:

- Support multi-language API descriptions by using Overlays to contain language translations.

- Provide configuration information for different deployment environments.

- Allow separation of concerns for metadata such as gateway configuration or SLA information.

- Provide default responses or parameters where they are not explicitly provided.

- Apply configuration data globally or based on filter conditions.

How do you apply the updates required deterministically based on a known location in the description and an explicit instruction set? This is an easy decision for human beings as they'll use their judgment, but it is more difficult for tooling makers, leading to opinionated decisions in their implementation. The same is true for many aspects of merging data to be included in an OpenAPI description to be published to your developer community or consumed by tooling. The use cases are varied and can include adding better tags for navigation in documentation or providing more metadata to generate SDKs. It is these challenges that Overlay aims to solve.

### Using the Overlay Specification

The [Overlay Specification](https://github.com/OAI/Overlay-Specification/blob/main/versions/1.0.0.md) works by adding a set of imperatives that specify how OpenAPI descriptions should be merged. This is encapsulated in an [Actions Object](https://github.com/OAI/Overlay-Specification/blob/main/versions/1.0.0.md#action-object) that prescribes the changes to be made, which is described in either an **update** or **remove** property. The instructions are applied using JSON Path, which points to a given property in the OpenAPI description.

The following are two examples from the Overlay Specification merged into one snippet:

```yaml
overlay: 1.0.0
info:
  title: Targeted Overlay
  version: 1.0.0
actions:
  - target: $.paths['/foo'].get
    update:
      description: This is the new description
  - target: $.paths['/bar'].get
    update:
      description: This is the updated description
  - target: $.paths['/bar']
    update:
      post:
        description: This is an updated description of a child object
        x-safe: false
  - target: $.paths.*.*.parameters[?@.name == 'sandbox-token']
    remove: true
```

The code snippet indicates the OpenAPI description should be updated with new values, namely:

- The `description` property at `$.paths['/foo'].get` is updated with a new value.

- The `description` property at `$.paths['/bar'].get` is updated with a new value.

- The Path Item at `$.paths['/bar']` is updated with a new `post` Operation Object.

- A parameter that matches the name `sandbox-token` in any Path Item and any Operation is removed.

### How Overlay Helps in Updating OpenAPI Descriptions

The previous snippet demonstrates a **_deterministic_** approach to merging information and serves the needs of the API lifecycle view of creating and using OpenAPI, which we've discussed in earlier chapters. Organizations can leverage this specification to update OpenAPI descriptions at different stages in the lifecycle and always expect consistent results when repeating the lifecycle stages. Overlay takes the guesswork out of how to approach this situation, which should benefit tooling makers and consumers of OpenAPI descriptions. The key benefit is flexibility, in that organizations can choose to update an OpenAPI description in a manner that suits their needs.

Please note that the Overlay Specification is currently an **implementer's draft** created to provide a means for the community to test the specification. This course will be updated in the future should any aspect change dramatically.

## Arazzo Specification (Workflows SIG)

### Describing Sequences of API Calls

In the examples we've looked at throughout this course, we've been looking at a single API described by an OpenAPI description. What about cases where there are multiple APIs that are linked together to form a use case or function that requires orchestration? The [Workflows SIG](https://github.com/OAI/sig-workflows) was formed to explore this use case. The goal of this SIG is to:

_"...propose an enhancement to the current OpenAPI, or accompanying specification (or means), that can define sequences of calls and their dependencies to be expressed in the context of delivering a particular outcome or set of outcomes."_

> _- OAI Workflows SIG: Motivation_

This goal has manifested itself in the [Arazzo Specification](https://github.com/OAI/sig-workflows/blob/main/versions/1.0.1.md). API providers can use this specification to provide a schematic representation of how to call several APIs and link them together using the data returned. Each Workflow description references one or more source documents, which, at version 1.0.0, can either be an OpenAPI description or a Workflow description.

### Describing a Workflow

The Specification itself shows a simple example. A [Workflow Object](https://github.com/OAI/sig-workflows/blob/main/versions/1.0.1.md#workflow-object) defines the workflow properties and any inputs external to the sequence of API calls (note multiple Workflow objects can be defined, hence the object is an array):

```yaml
- workflowId: loginUserAndRetrievePet
  summary: Login User and then retrieve pets
  description: This workflow lays out the steps to login a user and then retrieve pets
  inputs:
    type: object
    properties:
      username:
        type: string
      password:
        type: string
```

The Workflow object defines two input parameters, **username** and **password**, and provides other description properties.

### Describing Steps

The Workflow Object then defines a **steps** property, which is an array containing [Step Objects](https://github.com/OAI/sig-workflows/blob/main/versions/1.0.1.md#step-object). The Step Object defines the API calls that constitute the Workflow.

In the example, a Workflow consumer first calls the **loginStep** to get a token:

```yaml
- stepId: loginStep
  description: This step demonstrates the user login step
  operationId: loginUser
  parameters:
    # parameters to inject into the loginUser operation (parameter name must be resolvable at the referenced operation and the value is determined using {expression} syntax)
    - name: username
      in: query
      value: $inputs.username
    - name: password
      in: query
      value: $inputs.password
  successCriteria:
    # assertions to determine step was successful
    - condition: $statusCode == 200
  outputs:
    # outputs from this step
    tokenExpires: $response.header.X-Expires-After
    rateLimit: $response.header.X-Rate-Limit
    sessionToken: $response.body
```

To annotate the example:

- The step provides the list of parameters required to call the step. The input parameters **username** and **password** are required to initiate the workflow.

- The **successCriteria** property is also defined, which provides one or more **condition** properties that describe what success execution looks like.

- The **outputs** property defines dynamic values, using Runtime Expressions, that are accessible and possibly required for subsequent steps within the same workflow. The outputs are named so they can be easily referenced.

The Workflow consumer can then call the **getPetStep** to get the details of a given Pet:

```yaml
- stepId: getPetStep
  description: retrieve a pet by status from the GET pets endpoint
  operationPath: "{$sourceDescriptions.petstoreDescription.url}#/paths/~1pet~1findByStatus/get"
  dependsOn: loginStep
  parameters:
    - name: status
      in: query
      value: "available"
    - name: Authorization
      in: header
      value: $steps.loginUser.outputs.sessionToken
  successCriteria:
    - condition: $statusCode == 200
  outputs:
    # outputs from this step
    availablePets: $response.body
```

### How Arazzo Helps in Making Multiple API Calls

When we compare Arazzo to the OpenAPI Specification, we find that the Links object can help. Still, it lacks the deterministic sequencing model Workflows delivers and doesn't work when more than one API is involved. An API provider or tooling maker would need to use a significant number of Specification Extensions to facilitate workflow functionality, and, as we said earlier, doing this in isolation makes the efforts far less reusable.

Arazzo, therefore, provides a significant uplift for API providers in terms of how to describe sequencing API calls. This will also prove useful to tooling makers leveraging the specification to provide orchestration features in their software. Arazzo will provide ease of use for API consumers who will be able to orchestrate calls to multiple APIs far more seamlessly. Finally, Arazzo will make generated documentation more useful because it becomes easier to document more than just individual API endpoints.

## Knowledge Check

Congratulations on completing Chapter 6 - Extending OpenAPI. Take this quiz to check your understanding of the concepts you've learned about so far.

### Question 1

What is the purpose of a Specification Extension?

- [x] Provide a structured way to extend OpenAPI

- [ ] Provide a means to use OpenAPI with other specifications

- [ ] Allows additional HTTP methods to be supported in OpenAPI

- [ ] None of the above

### Question 2

How is a Specification Extension identified?

- [ ] Named in Title Case

- [ ] Included in the `extensions` array

- [x] Prefixed `x-`

- [ ] Registered in an IANA registry

### Question 3

Given the choices below, which one(s) are examples of how Specification Extensions are used?

- [ ] Provide additional metadata in Schema Objects

- [ ] Provide the means to configure an API gateway

- [ ] Display additional information to users of API documentation

- [x] All of the above

### Question 4

Ideally, when should you use Specification Extensions?

- [ ] Never

- [x] Sparingly, for specific requirements

- [ ] Sparingly, to help track versions

- [ ] Always, in every OpenAPI description

### Question 5

What is the purpose of SIGs in OAI ?

- [ ] Researching how Specification Extensions can be standardized

- [x] Providing a focus for improving OpenAPI usage in a given industry, subject area, or vertical

- [ ] Providing proposals for supporting additional HTTP methods

- [ ] Researching recipes of interest to the API community

### Question 6

What does the Overlay Specification do?

- [ ] Provides the means to add graphics to a rendered OpenAPI description

- [ ] Allows RPC-style APIs to be represented in OpenAPI

- [ ] Allow non-HTTP APIs to be represented in OpenAPI

- [x] Provides a deterministic way to apply updates to an OpenAPI description

### Question 7

Which of the following is an example of how an Overlay is used in the context of the API lifecycle?

- [x] Update Operation descriptions with copy-written text produced by a technical author before the document is published in a developer portal

- [ ] Add a timestamp to the filename of an OpenAPI description document

- [ ] Spellcheck an OpenAPI description document

- [ ] Change the encoding of the file from YAML to JSON

### Question 8

What does the Arazzo Specification do?

- [ ] Allows OpenAPI descriptions to be extended with asynchronous operations

- [ ] Provides an alternative approach to documenting asynchronous operations

- [ ] Describes common enterprise integration patterns

- [x] Allows a sequence of API calls to be described through a description language

### Question 9

How are external parameters specified in a Workflows description?

- [ ] In the `beforeAll` property at the root of the document

- [x] In the `parameters` array in the Workflow object

- [ ] In a source OpenAPI description

- [ ] Using a Specification Extension

### Question 10

What source documents can be used in version 1.0.0 of Arazzo ?

- [ ] OpenAPI and AsyncAPI documents

- [ ] OpenAPI and JSON Schema documents

- [x] OpenAPI and Arazzo Descriptions

- [ ] XML Schema documents
