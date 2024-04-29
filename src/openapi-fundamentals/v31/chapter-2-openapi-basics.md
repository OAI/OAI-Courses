# OpenAPI Basics

## Introduction

### Chapter Overview

The OpenAPI Specification provides a consistent syntax language to describe the shape of an API, providing a bridge between the expression of an API in code and the HTTP-based services it represents.

Understanding this structure and the syntax of the OpenAPI Specification is critical to using it effectively, as a tool to communicate with API consumers.

### Learning Objectives

By the end of this chapter you should understand:

- The basics of the HTTP-based APIs that typify the API Economy.
- How OpenAPI maps the features of HTTP-based APIs to its description language.
- The features OpenAPI provides that reflect the needs of API consumers.
- The basic structure of an OpenAPI description and why this provides an effective means of communication.

## HTTP, APIs and OpenAPI

### The role of HTTP

In Chapter 1 we discussed the growth of the API Economy and how this has been driven by an increasing number of web APIs that are built on HTTP. There’s no surprise that HTTP is the go-to choice as the protocol for providing web APIs. HTTP is the "language" of the web and providing APIs over the Internet is the _de facto_ choice for getting these products and services to target audiences quickly, effectively, and with minimal “plumbing” outside of the API providers stack. Web APIs routinely also implement JavaScript Object Notation - JSON - as the means to encode request and response payloads. These conventions have grown organically and reflect the preferences of both providers and consumers of web APIs.

OpenAPI is therefore primarily a means to describe HTTP-based APIs that largely, but not exclusively, provide JSON payloads. It does this by mapping the semantics of HTTP, either natively or in the REST architectural style [described](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) by Roy Fielding. There are, of course, other features implemented in OpenAPI that provide useful features for API providers to accurately describe their APIs.

### Mapping OpenAPI to HTTP

If you consider OpenAPI in terms of how it maps to HTTP it can be qualified as follows:

- HTTP is based on a system of [Uniform Resource Identifiers](https://datatracker.ietf.org/doc/html/rfc2616#section-3.2) (URIs). URIs incorporate a given domain name or IP address and the path at the server the resource is hosted at to provide a unique reference to a resource or entity. In OpenAPI this is a **Path**, which is defined using a **Paths Object** and contains one or more **Path Item Objects**.
- HTTP provides methods that can be used to retrieve or change the state of a given resource or entity - GET, POST, PUT, and so on. A Path Item Object therefore implements an **Operation Object** that provides the means to describe how an HTTP method is implemented in the API.
- Each Operation Object references an array of **Parameters Objects** that reflect the different types of parameters an HTTP URI can support - query parameters, HTTP headers, and cookies. OpenAPI also extends this to define **Path** parameters that describe a placeholder for a fragment of the URI that can be replaced by the API consumer (more on this later).
- Some HTTP methods also support sending a message payload to the server, which can be acted on to create a resource or execute a given operation. In OpenAPI this maps onto a **Request Body Object**.
- HTTP defines a huge number of possible response [status codes](https://tools.ietf.org/html/rfc7231#section-6), each providing a predefined coarse-grained indicator of the success or failure of the requested operation. The Operations Object provides a **Responses Object** that describes the return codes defined by the API and their associated properties (note there is an open-world assumption that other return codes are possible due to the distributed nature of the Internet).
- The Responses Object references one or more **Response Object** definitions that describe the response payloads. Each response is qualified by the content type, with HTTP headers described as required.

These mappings demonstrate the strong association between HTTP and OpenAPI and the basis of the model underpinning the OpenAPI language. Whilst there are protocols overlaying HTTP that are more difficult to map - for example, representing WebSockets in a way that is not overly complex - the association with HTTP means that OpenAPI can cover a wide range of design choices.

OpenAPI also uses several supporting technologies to underpin the Specification:

- **JSON and YAML**: An OpenAPI description document is encoded in either JSON or YAML (both are supported as first-class citizens).
- **JSON Schema**: JSON Schema is used to provide the means to define the properties of an object - defined as a **[Schema Object](https://spec.openapis.org/oas/v3.1.0#schema-object)** in OpenAPI. A Scheme Object is used to describe the format of request and response payloads, parameters, and headers.
- **Markdown**: [CommonMark](https://commonmark.org/) provides the syntax for adding descriptive text to an OpenAPI description document intended for human beings to read.

These features provide the basis of both the syntax and structure for creating a usable API description document. The specification language itself, however, is the key to providing what API providers need to describe their APIs effectively. We'll walk through each object in turn and discuss its relevance to accurately describing an API.

### Versions of OpenAPI

Before breaking down the structure of OpenAPI it is important to highlight the versions of the Specification currently available:

- Swagger, was retrospectively labeled 2.0 after it was donated by SmartBear.
- Swagger became the baseline for 3.0, which was published in 2017.
- The latest version, [3.1](https://spec.openapis.org/oas/v3.1.0.html), was published in February 2021.

A new major version, currently codenamed Moonwalk, is [being developed](https://www.openapis.org/blog/2023/12/06/openapi-moonwalk-2024). The goal is to make version 4 of OpenAPI general availability in 2024.

Throughout the the course wherever we refer to OpenAPI we mean version 3.1. All versions up to 3.1, however, mirror the features of HTTP as described above. If you are using a version earlier than 3.1 the object definitions may differ slightly, but the relationship to HTTP remains largely the same.

## High-Level Structure

### Structure Overview

An OpenAPI description has a standard structure prescribed by the description language with each part serving to communicate a part of the structure of the implementer’s API, with several objects at the root of the description document. This is described by the [OpenAPI Object](https://spec.openapis.org/oas/v3.1.0.html#openapi-object), which references several objects including:

- **Info Object**: Provides high-level information about the API being described.
- **Paths Object**: Describes the operations the API provides.
- **Components Object**: The parent object that houses all reusable objects within a given OpenAPI description.

These objects reference, for the majority of users, the most frequently used objects in OpenAPI. We’ll look at each of these in more detail as we progress through the chapter.

### Providing Information

It’s no surprise that providing information to end users of an API description document is served by the **[Info Object](https://spec.openapis.org/oas/v3.1.0.html#info-object)**. It provides the means to describe high-level information including the title, summary, and description information that applies to the entire API and other usage aspects such as the license and the terms of service.

The Info Object also provides a **version property**, which allows API providers to label a given document with a version number, often using [Semantic Versioning](https://semver.org/). This is an important feature of OpenAPI as it provides a standardized location for providing an unequivocal “stamp” that allies a given OpenAPI description to the operations, behaviors, and data that an API consumer will expect to find at a provider’s API:

![The Info Object at the root of the OpenAPI Object](./images/chapter-2-openapi-object.png)

The Info Object is also notable as the description property supports the means to add extended additional information using Markdown. The code snippet below shows a minimal example of an Info object:

```yaml
info:
  title: OpenAPI Basics API
  description: An example of an Info Object in an OpenAPI description
  version: 0.0.1
```

We can very quickly extend the example description over multiple lines and implement other Markdown features such as tables and an image:

```yaml
info:
  title: OpenAPI Basics API
  description: |
    An example of an Info Object in an OpenAPI description

    ## Introduction to API

    This provides a high-level summary. An image is provided below:

    ![Image embedded in OpenAPI description](example-image.png)

    These are the services levels available:

    | Name | Description |
    | --- | --- |
    | Basic | Free tier available to all consumers |
  version: 0.0.1
```

The important point here is that tooling can then render this information in a human-friendly format. The screenshot below uses [Redoc](https://github.com/Redocly/redoc) as an example:

![An example of an Info Object rendered with Redoc](images/chapter-2-rendered-document-without-tags.png)

The Info Object can therefore provide the means to extend the headline information that an OpenAPI description can deliver. This feature provides considerable capabilities for API providers to use OpenAPI as the spine of their documentation, pulling together both human- and machine-orientated information into a single format. Many API providers use this feature to considerable effect, which we'll look at in more detail in Chapter 4.

## Describing API Shape

### URLs, Paths, and Methods

The most significant section in an OpenAPI description is the **[Paths Object](https://spec.openapis.org/oas/v3.1.0.html#paths-object)**. The Paths Object is the key resource for API consumers in that it associates a given URI and HTTP method to one or more Operations.

Take this cutdown version of the classic Petstore API as an example:

```yaml
/pets/{petId}:
  get:
    summary: Info for a specific pet
    operationId: showPetById
    tags:
      - pets
    parameters:
      - name: petId
        in: path
        required: true
        description: The id of the pet to retrieve
        schema:
          type: string
    responses:
      "200":
        description: Expected response to a valid request
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Pet"
      default:
        description: unexpected error
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Error"
```

We can explain these features as follows:

- Paths is a Map that uses a URI to identify a given [Path Item Object](https://spec.openapis.org/oas/v3.1.0.html#path-item-object). In the code snippet above the URI `/pets/{petId}` is identified, which a Client must call to invoke one of the supported methods (Note that fragments of the URL in this example are placeholders - Path Templates - for parameter values, which we'll discuss in [later](#providing-parameters)).
- Each Path Item Object has one or more [Operation Objects](https://spec.openapis.org/oas/v3.1.0.html#operation-object)](https://spec.openapis.org/oas/v3.1.0.html#operation-object). These provide the HTTP methods that are supported at the URI. Each Operation can be uniquely identified in a given OpenAPI description with the property `operationId`.
- Each Operation, as well as identifying the supported HTTP methods, provides summary and description information and tags, then references one or more parameters expressed as [Parameter Objects](https://spec.openapis.org/oas/v3.1.0.html#parameter-object), where applicable a [Request Body Object](https://spec.openapis.org/oas/latest.html#request-body-object) and [Response Objects](https://spec.openapis.org/oas/v3.1.0.html#response-object) (encapsulated with [Media Type Objects](https://spec.openapis.org/oas/v3.1.0.html#media-type-object)). Responses are referenced through a map of possible HTTP return codes, with a `default` option that can be provided as a catchall as shown in the code snippet.

### Relationship between Paths, Path Items and Operations

Paths, Path Items, and Operations therefore provide the binding between the URIs that are exposed, the methods supported at each URI, and the shape of the requests and responses for each operation.

The model below shows how these objects relate to each other:

![Paths, Path Items and Operations](./images/chapter-2-paths-object.png)

It's worth noting that at version 3.1 of OpenAPI a Path Item Object can be reused directly i.e. a given combination of URL, method, parameter, and request/response body can be defined in the `pathItems` property in the Components Object. There are instances where this might be desirable. For example, an organization may choose to template their definition for a health-check endpoint across all APIs and resolve them to a given Path Item Object to the correct definition. This feature has considerable power for creating organization-wide templates for reuse, and is discussed in more detail [below](#defining-reusable-components).

## Describing Parameters, Requests and Responses

### Providing Parameters

URLs, Paths, and Methods are, however, only part of how API providers typically define the operations supported by their API. Parameters - of different kinds - are critical to allowing API consumers to invoke a given operation with the correct arguments. In HTTP terms we generally understand parameters are represented in a [Query](https://datatracker.ietf.org/doc/html/rfc3986#section-3.4), with parameters passed that can influence the retrieval of information from the URL in question.

In OpenAPI the idea of parameters is extended to incorporate other means to pass information when invoking an operation through the [Parameter Object](https://spec.openapis.org/oas/v3.1.0.html#parameter-object). The OpenAPI Specification specifics four types of parameters, namely:

- **Path**: A part of the URL, denoted using handlebar syntax in the Path Item Map. The specification provides the example `/items/{itemId}`, with the Petstore example being defined above as `/pets/{petId}`. In practical terms what this means for an API consumer is that this value **_can change_** at each invocation of a given operation, and the consumer needs to pass the appropriate information relevant to the context of the invocation i.e. to retrieve information on a given item or pet in our examples. APIs that follow the REST architectural style will most likely make extensive use of Path Parameters, using them to identify a given resource in a collection of resources.
- **Query**: Query Parameters reflect the Query string as described above. API providers often specify query parameters as optional arguments that can be used to modify the behaviors of a given operation. An oft-quoted example is for filtering a collection of resources when addressing a collection like `/pets`. An API provider might allow retrieval of all Pets, but provide the query parameter `petType` so API consumers can retrieve pets of a given type - Cat, Dog, etc. Variations on this theme are myriad.
- **Header**: Header parameters are [HTTP headers](https://httpwg.org/specs/rfc7230.html#header.fields), specifically request parameters in this context. Headers can also be defined [elsewhere](https://spec.openapis.org/oas/v3.1.0.html#header-object) and be referenced in an [Encoding Object](https://spec.openapis.org/oas/v3.1.0.html#encoding-object).
- **Cookie**: Cookies are also supported, allowing cookie data to be specified as a parameter.

A Parameter Object provides a common construct to define the attributes of the parameter in question. Take the Petstore example above and the parameter `petId`:

```yaml
name: petId
in: path
required: true
description: The id of the pet to retrieve
schema:
  type: string
```

The `petId` parameter is specified as a Path parameter., It includes a description property, whether the parameter is mandatory, and is declared with a type definition using a Schema Object that specifies the data type of the parameter. API consumers can therefore easily understand and implement parameter handling for the APIs they consume.

### Creating Request Body and Response Objects

Request Body and Response Objects are critical to conveying what is one of the most important features of OpenAPI, namely: What does the data look like? Having the means to describe the properties of a payload for a given operation is critical to successfully communicating what an API consumer needs to know. OpenAPI would be a much less powerful tool if this aspect of the description language did not exist.

All Request Body and Response Objects provide a description of how the data is encoded, which is done using a Media Type Object. In the examples you've seen so far the format of the request or response payload can be defined with a property like `application/json`. This value will provide the value of the `Content-type` header at runtime.

![The relationship between Request Body and Response Objects, Content type, and Media Type Objects](./images/chapter-2-content-field.png)

The Media Type Object includes the property `schema`, which defines or references a Schema Object. We mentioned the fact that OpenAPI outsourced the semantics of defining a Schema Object to JSON Schema in our introduction, with each specification referencing a different JSON Schema version. [Draft 2020-12](https://tools.ietf.org/html/draft-bhutton-json-schema-00) is supported at version 3.1, with what is described as a "superset" of JSON Schema in the Specification itself. What this means in practical terms is that users of OpenAPI are free to use JSON Schema features in their Request and Response Objects, with the underlying Schema objects providing the dictionary.

API providers can therefore shape these objects using a rich vocabulary encapsulated in an object definition. For example, to send a simple list of names a Schema object can be implemented as follows:

```yaml
type: object
properties:
  names:
    type: array
    items:
      type: string
```

This example uses the `array` type to describe a list, with each value of `items` being of the type `string`. We may, however, want to restrict the length of the names so we can quickly add `minLength` and `maxLength` properties, and also restrict the length of the array itself using `maxItems`:

```yaml
type: object
properties:
  names:
    type: array
    items:
      type: string
      minLength: 1
      maxLength: 100
    maxItems: 5
```

If we want to add restrictions on the format of the data - perhaps ensuring something simple like there is only a single word in the name property - we can add a pattern:

```yaml
type: object
properties:
  names:
    type: array
    items:
      type: string
      minLength: 1
      maxLength: 100
      pattern: ^\w$
    maxItems: 5
```

We can see from this simple example how JSON Schema allows us to quickly build up a picture of the data we expect to receive or return at our API. We can then create a Request Body or Response Object by enclosing the Schema Object in a Media Type Object as we mentioned above. For example, a Request Body Object that is expected to be received in JSON can be defined as follows based on the snippet above. The `required` keyword is also included in this snippet. This indicates that the property `names` must be defined in the request body:

```yaml
description: Request body containing expected strings
content:
  application/json:
    schema:
      type: object
      required:
        - names
      properties:
        names:
          type: array
          items:
            type: string
            minLength: 1
            maxLength: 100
            pattern: ^\w$
          maxItems: 5
```

A Response Object can be defined as follows, which includes expected response HTTP headers:

```yaml
description: Response payload including expected HTTP headers
headers:
  "x-example-header":
    description: Example header using deprecated x- nomenclature
    schema:
      type: string
content:
  application/json:
    schema:
      type: object
      required:
        - names
      properties:
        names:
          type: array
          items:
            type: string
            minLength: 1
            maxLength: 100
            pattern: ^\w$
          maxItems: 5
      additionalProperties: false
```

We also set `additionalProperties` to `false` in this example, which provides an indicator for parsers that only the properties described in the Schema Object should be expected in the payload. Note that this property is not recursive, so needs to be set wherever it applies in a nested Schema object structure.

Schema Objects are not restricted solely to Request and Response payload and are used to define schema definitions for Header and Parameter Objects as well. Being able to leverage JSON Schema to define such requirements is important across OpenAPI. The important thing to note in the context of the examples above is that an API provider can support more than one content type, perhaps adding `text/xml` to the payload encoding they support (note that for XML there are specific properties that can be leveraged, which we don't go into in detail in this course). In such cases declaring the Schema Object inline for each Media Type is suboptimal, and a reusable definition is useful. This stands across the vast majority of OpenAPI objects, and object reuse is therefore an important topic.

Finally, you can also leverage schema composition keywords from JSON such as `allOf` and `oneOf`. These allow you to combine Schema objects as a means to combine Schema objects (with [restrictions](https://spec.openapis.org/oas/v3.1.0#composition-and-inheritance-polymorphism)) with `allOf` or provide optionality through `oneOf`. Schema composition can help you make the most of reuse opportunities in your OpenAPI descriptions.

## Defining Reusable Objects

### Objects That Can Be Reused

So far we've focused on describing properties in the context of where they are used _inline_ within an OpenAPI description (there are examples of reuse in the snippets above, but we don't discuss them). There are, however, many very strong use cases for creating reusable object definitions. This is where the [Components Object](https://spec.openapis.org/oas/v3.1.0.html#components-object) comes in. The Components Object provides a standardized location for storing reusable objects. The vast majority - although not all - of reusable objects are enclosed by the Component object.

The available properties are as follows (not all of which are described above):

- Callbacks
- Examples.
- Headers
- Links
- Path Items
- Parameters
- Request Bodies
- Responses
- Schemas
- Security Schemes

Each object defined in one of these properties can then be referenced using a [Reference Object](https://spec.openapis.org/oas/v3.1.0.html#reference-object).

### Example of Object Reuse

In our Petstore snippet [above](#urls-paths-and-methods) we already show how Component properties can be referenced using a Reference Object. Reference Objects are supported by [rules](https://spec.openapis.org/oas/v3.1.0.html#relativeReferencesURI) for resolving URIs. If we were to template the Path Item above - because reusing this object has value - the example can be refactored as follows (using placeholders for the Schema Objects):

```yaml
paths:
  /pets/{petId}:
    $ref: "#/components/pathItems/petById"
components:
  pathItems:
    petById:
      get:
        summary: Info for a specific pet
        operationId: showPetById
        tags:
          - pets
        parameters:
          - name: petId
            in: path
            required: true
            description: The id of the pet to retrieve
            schema:
              type: string
        responses:
          "200":
            description: Expected response to a valid request
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/Pet"
          default:
            description: unexpected error
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/Error"
  schemas:
    Pet:
      type: object
    Error:
      type: object
```

This approach stands true for all objects that the Components object supports. References can also be remote, meaning external OpenAPI descriptions (or JSON Schema documents) can be referenced. This feature has immense power, especially in our use case of a standardized health check object; organizations can define the required object once and then reference it from all APIs. Such an approach - when coupled with linting using relevant tools - can help provide design-time governance for APIs (we go into more detail on this in Chapter 4).

## Other Features

### Grouping Operations using Tags

One feature of OpenAPI commonly used by API providers is [Tags](https://spec.openapis.org/oas/v3.1.0.html#tag-object). A Tag object is a label and description that allows API providers to group operations by the label value, which for tooling makers who support providing documentation is important.

To provide an example, in the screenshot in the [Providing Information](#providing-information) topic a tag we defined "This is an example". By defining a Tag object we add a description:

```yaml
tags:
  - name: This is an example
    description: An example of providing a tag for an Operation
```

We can enrich the information that Redoc displays:

![Example of rendered view with Tags implemented](images/chapter-2-rendered-document-with-tags.png)

Note the difference between the first and second screenshots. The second contains both the Tag name, which is rendered as an expandable navigation menu item, and the description at the start of the section. Tags therefore provide a convenient way to group Operations that can increase the usability of documentation. It should also be noted that a tag is always referenced by its name and not using a Reference Object, which is a feature it has in common with [Security Requirements](#describing-security-requirements).

### Describing Security Requirements

The context of our course so far has been largely that of the increasing popularity of web APIs and as a consequence the growth of the API Economy. The security of a provider’s APIs in this context is of paramount importance as a breach could result in significant financial loss. This is especially true in verticals like financial services where API traffic accounts for an increasing proportion of payment instructions.

The OpenAPI Specification therefore provides the means to reflect security details through an API description document. Such features are over and above that provided by core HTTP as security protocols are typically built on top of the transport mechanism.

### Supported Security Requirements

OpenAPI currently provides support for five different security schemes through the **[Security Scheme Object](https://spec.openapis.org/oas/v3.1.0.html#security-scheme-object)**, including the following:

- **API Key** (`apiKey`): API keys are a popular means for providing a coarse-grained security credential to API consumers. Whilst the popularity of API keys has waned somewhat - largely due to the fact they are not protocol-bound and therefore not standardized and because they provide limited proofs-of-possession - they continue to be provided in OpenAPI.
- **HTTP** (`http`): HTTP provides a pointer to any valid security scheme in the [IANA Authentication Scheme registry](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml). Whilst there are several entries in this registry, probably the most popular are [Basic Authentication](https://www.rfc-editor.org/rfc/rfc7617.html) - essentially a username and password - and [Bearer Tokens](https://www.rfc-editor.org/rfc/rfc6750.html) in the context of OAuth 2.0.
- **Mutual TLS** (`mutualTLS`): Mutual TLS is a security mechanism that is popular in financial service APIs as it enforces the verification of x509 certificates at both the client and the server. OpenAPI provides limited built-in metadata for this Security Scheme, and API providers must provide additional details to describe specifics like accepted certificate authorities and supported ciphers.
- **OAuth 2.0** (`oauth2`): OAuth 2.0 is a fundamental building block of the API Economy as it facilitates allowing users - real human beings - to delegate their access to a third party at a given service provider. It is therefore well represented in OpenAPI, with the means to describe the [most important](https://spec.openapis.org/oas/v3.1.0.html#fixed-fields-24) OAuth flows.
- **OpenID Connect** (`openIdConnect`): Support for OpenID Connect is supported in providing a link to the OpenID Connect Discovery metadata. Whilst this in itself does not provide much in the way of rich metadata it provides a pointer to a very rich document that can be programmatically parsed, allowing API consumers to access and act on this information in their applications in an automated manner.

Each of these can be applied to a given Operation Object, or defined globally at the root level of the OpenAPI description, as shown in the following diagram:

![How Security Requirements are Implemented in OpenAPI](./images/chapter-2-security-object.png)

### Security Requirement Example

In the snippet below the Petstore example has been amended to provide an example.

HTTP Basic Authentication is required globally, but an API key is required specifically for a `get` on the `/pets/{petId}` Path Item:

```yaml
openapi: 3.1.0
info:
  title: Petstore Snippet
  version: 0.0.1
security:
  - basicAuth: []
paths:
  /pets/{petId}:
    get:
      security:
        - apiKey: []
      summary: Info for a specific pet
      operationId: showPetById
      tags:
        - pets
      parameters:
        - name: petId
          in: path
          required: true
          description: The id of the pet to retrieve
          schema:
            type: string
      responses:
        "200":
          description: Expected response to a valid request
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Pet"
        default:
          description: unexpected error
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
components:
  schemas:
    Pet:
      type: object
    Error:
      type: object
  securitySchemes:
    apiKey:
      description: API Key
      type: apiKey
      name: api-key
      in: header
    basicAuth:
      description: Basic Authentication
      type: http
      scheme: basic
```

It should be noted that these Security Scheme Object definitions are relatively coarse-grained, and provide only the basic information to indicate what security requirements. API providers need to provide more information - especially around onboarding and credential rotation - that sits outside the scope of OpenAPI. You should also note the relevance of the empty array in Security Requirement objects. This is populated for OAuth Flow and OpenID Connect objects to provide the scopes that apply to the Operation. An empty array is provided in all other cases.

However, OpenAPI still provides a strong indicator of the security requirement and, with the judicious use of descriptions and pointers to other external resources, it still serves to provide a comprehensive description of the API for consumers.

### Using Specification Extensions

The last feature of OpenAPI that needs mentioning at this point is [Specification Extensions](https://spec.openapis.org/oas/v3.1.0.html#specification-extensions). This object provides the means for implementers or API providers to follow a standardized pattern for extending the OpenAPI specification. They can provide additional properties in the OpenAPI description, prefixed with `x-`, to denote that the property is not a core OpenAPI property. This allows tooling makers to easily identify Specification Extensions and ignore them where they do not support them or are not relevant.

This is useful where, for example, a vendor can provide arguments that are not covered in the core specification for configuring their tools. Taking an example from an OpenAPI member, SmartBear provides extensions in their [SwaggerHub](https://support.smartbear.com/swaggerhub/docs/en/manage-apis/swaggerhub-vendor-extensions.html) product to enhance certain features of the product, including integrating SwaggerHub with external API gateway providers.

Guidance for this feature is relatively limited in the specification itself as it is used at the behest of implementers. It can provide, however, a very powerful means for extending OpenAPI whilst preserving the core of the specification.

## Course Scope

### Features Not Covered Here

In this chapter we’ve learned the fundamentals of OpenAPI including the basis of the structure, how it relates to HTTP, and other technologies that support the delivery of the specification itself. We’ve also looked at API security and how it is expressed in the specification and what Specification Extensions are with an example of how they can be used.

Our list isn't exhaustive. For example:

- [Server Object](https://spec.openapis.org/oas/v3.1.0.html#server-object): Provides details on where a given API is available. We'll introduce this in more detail in Chapter 4.
- [Callback Object](https://spec.openapis.org/oas/v3.1.0.html#callback-object): Allows API providers to describe a dynamic callback mechanism in their OpenAPI description that allows them to call an endpoint provided by an API consumer out-of-band.
- [Link Object](https://spec.openapis.org/oas/v3.1.0.html#link-object): Provides links between a given response and a subsequent request. This feature is less used in the wild, and therefore we do not cover it here.
- The `webhook` property, a root property of the [OpenAPI Object](https://spec.openapis.org/oas/latest.html#fixed-fields): Can be used to define the Webhooks an API consumer can expect to receive from the API provider and provides a template for implementation (in a similar way that the OpenAPI description can do this). This property is a Map of Path Items and follows the same semantics, except for the fact that they are identified by object name rather than a Map of Paths.

What we've discussed are the core features of the OpenAPI Specification. As version 4 of OpenAPI evolves we'll revisit our course content and offer revisions that take the same approach, highlighting the most frequently-used features and offering appropriate guidance on their implementation. We'll also provide a full list of useful resources you can use to further your knowledge on the topics we have not covered at the end of the course.

## Knowledge Check

Congratulations on completing Chapter 2 - OpenAPI Basics. Take this quiz to check your understanding of the concepts you've learned about so far.

### Question 1

What object in OpenAPI is used to define the available URIs for a given API?

- [ ] Info
- [ ] Sidewalk
- [x] Paths
- [ ] Path Item

### Question 2

In which object would you find the `version` property?

- [x] Info
- [ ] Components
- [ ] Description
- [ ] Summary

### Question 3

What can be used to add formatted descriptions to OpenAPI descriptions?

- [ ] AsciiDoc
- [x] Markdown
- [ ] Latex
- [ ] Plain text

### Question 4

A Path Item object provides one or more what, identified by an HTTP method?

- [x] Operations
- [ ] Parameters
- [ ] Servers
- [ ] Descriptions

### Question 5

What property can be used to specify a standard response that will be received if no return code is specified?

- [ ] `standard`
- [ ] `xxx`
- [ ] `all`
- [x] `default`

### Question 6

Which of the following are valid Parameters Object types (choose 2)?

- [ ] `body`
- [x] `in`
- [ ] `text`
- [x] `query`

### Question 7

What description language is used to define Schema Objects?

- [ ] XML Schema
- [ ] grpc
- [x] JSON Schema
- [ ] RDF

### Question 8

Which of the following is **_NOT_** available in the Components Object?

- [ ] Headers
- [ ] Parameters
- [x] Servers
- [ ] Path Items

### Question 9

Which of the following is **_NOT_** a supported Security Scheme in OpenAPI?

- [x] SAML
- [ ] API Key
- [ ] Basic Authentication
- [ ] Mutual TLS

### Question 10

What feature of OpenAPI can you use to extend the specification?

- [x] Specification Extension
- [ ] Markdown
- [ ] JSON Schema
- [ ] Remote References
