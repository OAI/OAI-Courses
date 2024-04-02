# Extending OpenAPI

Welcome to the fifth and final module of our OpenAPI v3.1 Fundamentals course.

In module 4 we looked at OpenAPI being applied in practice by walking through use cases, how OpenAPI facilitates the use cases and examples of tools from the community that help address them. We used sample OpenAPI documents and code snippets to provide more detail on how OpenAPI both reflects and communicates the shape of our APIs.

In this last module we look at how OpenAPI is extended, specifically:

- How tooling makers or large organization add their own properties to reflect specific requirements not covered directly in the specification.
- How other specification makers leverage OpenAPI to create standards that fulfil other use cases.

These are reflected in two areas of note: how Specification Extensions are used and how other specifications make use of OpenAPI.

Lets look at Specification Extensions first.

## Using Specification Extensions

[Specification Extensions](https://spec.openapis.org/oas/v3.1.0.html#specification-extensions) are a feature of the OpenAPI specification we have not covered in our earlier modules because their application is so wide. They provide a structured approach to extending a given OpenAPI document and can be used in virtually any object. They allow API providers and tooling makers to add their own customizations that complements their use cases or products.

Extension property names are always prefixed with `x-`. This indicates that they are not properties of the core OpenAPI specification and therefore should either be ignored or consumed based on a tooling maker or API consumer's understanding of what they represent. Any other guidance in the specification is relatively light as use of this object is left to implementers. The main benefit is to allow OpenAPI to be tailored to specific use cases and scenarios using a deterministic approach.

The easiest way of showing the utility of Specification Extensions is by exemplar. Take, for example, the UK open banking [Payment Initiation OpenAPI document](https://raw.githubusercontent.com/OpenBankingUK/read-write-api-specs/master/dist/openapi/payment-initiation-openapi.yaml). The specification implements an extension entitled `x-namespaced-enumeration`, which defines a list of values that apply to a given string-based property and are set by the standards body who created the document.

The example below shows some of the possible values of the property `ErrorCode` as specified in the standards:

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

You might be asking, why bother with this? Why not use an `enum` property? The answer lies in the appetite of the standards body for breaking changes, as specifying this list in an `enum` allied to a Response Object may make the OpenAPI document more brittle. This solution allowed the list to be published and be machine-readable, but without resulting in the brittleness that the standards body was trying to avoid. You could argue that this is just semantics and any changes to this list is a breaking change anyway, but it ensures that changes were isolated away from the enum value and therefore not disruptive when consumed by tooling.

This example, whilst not specifically for an API provider, shows how providing additional information to API consumers can be facilitated. Tooling makers can also follow a similar path in providing affordances for API providers to implement additional properties. A simple example is how Redoc [provides](https://github.com/Redocly/redoc?tab=readme-ov-file#openapi-specification-extensions) the means to customize their API documentation based solely on the content of Specification Extension properties, for example to swap out the Redoc logo:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
  x-logo: https://www.openapis.org/wp-content/uploads/sites/3/2018/02/OpenAPI_Logo_Pantone-1.png
```

One final example of using Specification Extensions is to help configure API-related infrastructure. Tooling makers often use Extensions to allow API providers using their tooling to provide additional configuration data.

The example below shows how this is supported in Azure API Management. Microsoft provides the extensions `x-ms-paths` to allow Path Item identifiers to include query parameters, in order to complement how their API Management product can be configured to serve traffic:

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

Note that this approach is opinionated - in that reflects what one organization thinks about this property - and serves the purposes of Microsoft and their product consumers.

There is, however, a point to make here. In the same vein as Microsoft you need to look hard at how you use Specification Extensions and how they can be leveraged to serve the needs of your API or tools. It goes without saying that wherever possible you should use the core OpenAPI Specification first and then leverage extensions only where strictly necessary. Remember that your API or tools are unlikely to the only one's your customer or API consumer uses. Making them deal with many different Extensions - unless there is a genuine need - is likely to degrade their experiences of your tools or APIs.

## Other Specifications

Specification Extensions provide the opportunity to "fill in the gaps" in the OpenAPI Specification where special cases or specific requirements dictate.

There comes a point, however, where the OpenAPI specification cannot do it all on its own. This is where other specifications help provide an approach or standards that fulfill a specific use case or addresses a given industry vertical. Some of these specifications coalesce around a Special Interest Group, or SIG, with a good number that are actively developing specifications.

We'll look at two specifications, namely Overlays and Workflows.

### Overlays

The Specification Extensions section showed how, relatively speaking, permissive the OpenAPI format is. However, this openness is something of a curate's egg in that it can be difficult to "know" how to deterministically process a given OpenAPI document. Take, for example, the Servers Object we discussed in Module 3. If in your API lifecycle you merge Servers data from an automatically generated OpenAPI document with information from configuration data represented in OpenAPI format, how do you deterministically process the correct data first? This is an easy decision for human being - as they'll use their judgement - but for tooling makers its more difficult, and leads to opinionated decisions in their implementation.

Overlays works by adding a set of imperatives that allow a provider to "instruct" how OpenAPI documents should be merged. This is encapsulated in an [Actions Object](https://github.com/OAI/Overlay-Specification/blob/main/versions/1.0.0.md#action-object) that prescribes the changes to be made, which is manifested in either an `update` or `remove` property. The instructions are applied by way of a JSON Path, which point to a given property in the OpenAPI document.

Merging two examples from the specification:

```yaml
overlay: 1.0.0
info:
  title: Targeted Overlays
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

The code snippet indicates the OpenAPI document should be updated with new values, namely:

- The `description` property at `$.paths['/foo'].get` is updated with a new value.
- The `description` property at `$.paths['/bar'].get` is updated with a new value.
- The Path Item at `$.paths['/bar']` is updated with a new `post` Operation object.
- A parameter that matches the name `sandbox-token` in any Path Item and any Operation is removed.

This clearly demonstrates a deterministic approach to merging information, and serves the needs of the API lifecycle view of creating and using OpenAPI that we've discussed in modules 3 and 4. Organizations can leverage this specification to update OpenAPI document at different stages in the lifecycle, and always expect consistent results when repeating the lifecycle stages. Overlays therefore serves to take the guesswork out of how to approach this, which should be of considerable benefit to tooling makers and consumers of OpenAPI documents.

> Overlays is currently an implementers draft created to provide a means for the community to test the specification as it stands. This course will be updated in the future should any aspect change drastically.

### Workflows

In the examples we've looked at throughout this course we've always been looking at a single API described by an OpenAPI document. What about cases where there are multiple APIs and those APIs are linked together to form a use cases or function that requires orchestration? It is for such use cases that the [Workflows SIG](https://github.com/OAI/sig-workflows) was formed. The goal of this SIG is:

_"...propose an enhancement to the current OpenAPI, or accompanying specification (or means), that can define sequences of calls and their dependencies to be expressed in the context of delivering a particular outcome or set of outcomes."_

This goal has manifested itself in version 1.0.0 _(release candidate)_ of the [Workflows Specification](https://github.com/OAI/sig-workflows/blob/main/versions/1.0.0.md). API providers can use this specification to provide a schematic representation of how to call several APIs and link them together using the data returned. Each Workflow document references one-or-more source documents, which at version 1.0.0 can either be an OpenAPI document or a Workflow document.

The specification itself shows a simple example. A [Workflow Object](https://github.com/OAI/sig-workflows/blob/main/versions/1.0.0.md#workflow-object) defines the workflow itself and any inputs external to sequence of API calls (note multiple Workflow objects can be defined, hence the object is an array):

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

The Workflow object defines two input parameters, `username` and `password`, and provides other description properties.

An API consumer first calls the `loginStep` to get an token:

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

- The step provides the list of parameters required to call the step. The input parameters, `username` and `password` are required to initiate the workflow.
- It also defines the `successCriteria` property, which provides one-or-more `condition` properties that describe what success execution looks like.
- The `outputs` property defines what is required to call a subsequent step, using Runtime Expressions to define the required values. These properties are named so they can be easily referenced.

The Workflow consumer can then call the `getPetStep` to get the details of a given Pet:

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

When we compare this to the native OpenAPI Specification we find that the Links object can help, but it lacks the deterministic sequencing model that the Workflows Specification delivers. An API provider or tooling maker would need to use a significant number of Specification Extensions to facilitate this and, as we said earlier, doing this in isolation makes the efforts far less reusable.

The Workflows Specification therefore provides a significant uplift for API providers in how to describe sequencing API calls. This will also prove useful to tooling makers who can leverage the specification to provide orchestration features in their software. Finally, and probably most important, the Workflow Specification will provide ease-of-use for API consumers who will be able to orchestrate calls to multiple APIs far more seamlessly.

## Plenary

In this module we've looked at how OpenAPI can be extended using Specification Extensions and provided concrete examples in the API economy of how API providers and tooling makers make use of Extensions to complement their support for OpenAPI.

We've also taken a look at other specifications and Special Interest Groups that use OpenAPI as a basis for delivery extending use cases.

This brings the OpenAPI v3.1 Fundamentals course to a close. We hope you've enjoyed it and it helps you use OpenAPI in your work in the future!

## Quiz

To help reinforce your knowledge please answer the following questions.

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

What are examples of how Specification Extensions are used?

- [ ] Provide additional metadata in Schema Objects
- [ ] Provide the means to configure an API gateway
- [ ] Display additional information to users of API documentation
- [x] All of the above

### Question 4

Ideally, when should you use Specification Extensions?

- [ ] Never
- [x] Sparingly, for specific requirements
- [ ] Sparingly, to help track versions
- [ ] Always, in every OpenAPI document

### Question 5

What does the abbreviation SIG stand for?

- [ ] Standardised Internet Grading
- [ ] Special Internet Group
- [x] Special Interest Group
- [ ] Significant Interest Group

### Question 6

What do SIGs aim to do?

- [ ] Look at how Specification Extensions can be standardized
- [x] Provide a focus for how OpenAPI can be extended in a given industry or vertical
- [ ] Provide proposals for supporting additional HTTP methods
- [ ] Research recipes of interest to the API community

### Question 7

What does the Overlays Specification do?

- [ ] Provides the means to add graphics to a rendered OpenAPI document
- [ ] Allows RPC-style APIs to be represented in OpenAPI
- [ ] Allow non-HTTP APIs to be represented in OpenAPI
- [x] Provides a deterministic way to merge multiple OpenAPI documents

### Question 8

What does the Workflows Specification do?

- [ ] Allows OpenAPI documents to be extended with asynchronous operations
- [ ] Provides an alternative approach to documenting asynchronous operations
- [ ] Describes common enterprise integration patterns
- [x] Allows a sequence of API calls to be described through a specification language

### Question 9

How are external parameters specified in a Workflow document?

- [ ] In the `beforeAll` property at the root of the document
- [x] In the `parameters` array in the Workflow object
- [ ] In a source OpenAPI document
- [ ] Using a Specification Extension

### Question 10

What source documents can be used in version 1.0.0 of the Workflow Specification?

- [ ] OpenAPI and AsyncAPI documents
- [ ] OpenAPI and JSON Schema documents
- [x] OpenAPI and Workflow documents
- [ ] XML Schema documents