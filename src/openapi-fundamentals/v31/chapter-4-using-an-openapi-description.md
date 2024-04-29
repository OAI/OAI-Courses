# Using an OpenAPI description

## Introduction

### Chapter Overview

OpenAPI descriptions provided by API providers can be used by API consumers in many different ways, many of which can be qualified in the stages of the API lifecycle we introduced in Chapter 3.

Activities API consumers can use an OpenAPI description for generating documentation, generating an API client, applying governance to API design, and many other activities. Such activities support API consumers in performing their roles more accurately and efficiently.

### Learning Objectives

By the end of the chapter you should be able to:

- Understand how OpenAPI supports activities of an API lifecycle.
- Evaluate how OpenAPI is applied based on several use cases and examples.
- Apply this knowledge to further your use of OpenAPI in your organization's API lifecycle.

## Using an OpenAPI description and the API lifecycle

### The API Lifecycle

In Chapter 3 we introduced a hypothetical API lifecycle. This was created by the OpenAPI Initiative to explain how OpenAPI can be used throughout the development and deployment of APIs:

![The API lifecycle as imagined by OpenAPI Initiative](https://www.openapis.org/wp-content/uploads/sites/3/2023/05/What-is-OpenAPI-Simple-API-Lifecycle-Vertical.png)

Each stage in this lifecycle is associated with different organizational roles, with a variety of wants and needs from the people partaking in each stage. This determines a great number of use cases for API-related documentation, driven by those activities. Some of these may already be familiar to you, whilst others may be novel in terms of your experiences with APIs. To draw out some of these we'll look at several common use cases and provide examples of toolsets that show how an OpenAPI description is leveraged to fulfill the use cases.

Please note that - being an open format - OpenAPI can be used in a huge number of ways depending on the perspective of the API consumer, specific developers, and tooling makers. We are only covering very common activities here.

## Generating API Documentation

### Use Case for Generating API Documentation

Our first use case is generating documentation, which is a feature of the Publish stage of an API lifecycle. You might question why this is so, given the fact that an OpenAPI description is a document encoded in JSON or YAML with a specific structure.

Even the bare minimum of information in an OpenAPI description tells us something about the shape of an API. The inclusion of Markdown in the specification, however, means that `description` properties can be very rich, including formatting and links to graphics. An OpenAPI description can therefore provide the spine of the documentation, with Markdown content providing the "meat on the bone". Toolsets have therefore evolved that use the content of the OpenAPI description to drive the rendering of human-orientated documentation built for browsing the operations the API supports

### Example of Generating API Documentation

You can get a sense of how rich this can be by looking at some examples in the wild. Take, for example, the organization Zuora who provides documentation using Redoc. Their [API documentation](https://developer.zuora.com/api-references/api/overview/) is very comprehensive, providing developers with everything they need to know about the operations the API supports. Not all the content is embedded in the OpenAPI description as it's too voluminous to manage there, but the structure serves to tie the information together.

### Task: Generate API documentation using Redoc

Redoc is an open-source tool - you saw a screenshot in Chapter 3 - and an easy way to provide an example of generating documentation.

Follow [the example](https://github.com/OAI/OAI-Courses/blob/main/chapter-4-examples/generating-documentation/README.md) of using Redoc with our [design-first OpenAPI description](https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-v31-fundamentals/chapter-3-examples/design-first-example/design-first-example-openapi.yaml) if you want to explore publishing documentation in more detail.

## Generating an API Client

### Use Case for Generating an API Client

Our first use case shows how API providers dogfood their OpenAPI descriptions to help publish documentation. It makes sense, however, for these providers to also publish OpenAPI descriptions directly to API consumers. Human-focused documentation is only part of the needs of API consumers - they also want the description itself to feed their tools.

This is another key aspect of the Publish stage in our lifecycle. We've already looked at design-first versus code-first as the means for creating your OpenAPI description document. Regardless of the approach, a some point - obviously - an API consumer will want to do something with your OpenAPI description document.

One example of how an OpenAPI description can be used for creating software clients based on the structure of the API. This is usually done by processing the description and performing code generation in a target language. There is an **_enormous_** number of tools that will do this for you, with your choice based on support for your programming language or application framework.

### Example of Generating an API Client

One such tool is [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/) from Microsoft. The idea of this tool is to provide a consistent API client experience without sacrificing extensibility, with API access wrapped around a given object. Take an example written in C# from the [Kiota](https://learn.microsoft.com/en-us/openapi/kiota/experience#create-a-resource) documentation:

```c#
// An authentication provider from the supported language table
// https://github.com/microsoft/kiota#supported-languages, or your own implementation
var authProvider = ;
var requestAdapter = new HttpClientRequestAdapter(authProvider); // Transport provider over HTTP
var client = new ApiClient(requestAdapter);                      // The generated API client package
var user = await client.Users["bob@contoso.com"].GetAsync();

var newUser = new User
{
    FirstName = "Bill",
    LastName = "Brown"
};

await client.Users.PostAsync(newUser);
```

The developer uses the `ApiClient` object to interact with the API, simplifying the integration effort. This is obviously both a simple example and can also be achieved with many other toolsets. The point is, however, that it seamlessly meets the goal of passing knowledge from the API provider to API consumers, who can use that knowledge in as near automated fashion as possible. This can provide a significant boost for developers who do not need to handcraft a client to access a given API.

We've picked generating an API client as a use case, but you can extend the scope of this back into the Configure stage of our API lifecycle. Many tooling vendors - especially those in the API management space - leverage OpenAPI descriptions to configure infrastructure such as API gateways. Typically these will be enhanced with Specification Extensions, which we will cover in Chapter 5.

### Task: Generating an API Client using Kiota

Kiota supports [a number](https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/) of programming languages.

Use one of the quick-start guides in your choice of programming language to explore generating an API client in more detail.

Use our [design-first OpenAPI description](https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-v31-fundamentals/chapter-3-examples/design-first-example/design-first-example-openapi.yaml) as an input to your API client.

## Applying Governance

### Use Case for Applying Governance

In our first two use cases, we've focused largely on meeting the needs of API consumers by providing an OpenAPI description to help in their goal of integrating with your APIs. There are other ways we can leverage our OpenAPI description before we get to the point of publishing it to API consumers. One area is that of ensuring our APIs adhere to our internal standards for design, which is often called **_design-time governance_**. This style of governance is an essential part of the API lifecycle in many organizations and ensures that when APIs are published to consumers they are designed to be consistent and fit for purpose.

Whilst this style of governance is not a silver bullet - as the design itself needs to be implemented in software, which needs to be tested - it can help catch design issues do not conform with how an organization wants to design its APIs. You need, of course, to create or generate your OpenAPI descriptions early enough in the API lifecycle to succeed in this style of governance, but it can reap rewards for your organization.

### Example of Applying Governance

One example of a tool that can help you apply design-time governance is [Spectral](https://stoplight.io/open-source/spectral), which uses style guides codified as "rulesets" to work as a design linter. Spectral is an open-source command-line tool and can be deployed virtually anywhere.

The following is a simple example of a Spectral ruleset:

```yaml
extends: spectral:oas
rules:
  security-must-be-enforced-for-unsafe-endpoints:
    message: You need a Security Requirement for unsafe operations
    severity: error
    given: "$.paths.*[?(@property == 'post' || @property == 'put' || @property == 'patch' || @property == 'delete')]"
    then:
      - field: security
        function: truthy
```

To annotate the example:

- The ruleset extends Spectral's default ruleset for OpenAPI (`extends: spectral:oas`).
- The `rules` property allows you to specify one or more design rules with each uniquely identified with a name.
- Each rule provides a message and severity to drive how the correct behaviors when an error is encountered.
- A JSON Path is also specified to indicate the object to which the rule applies in an OpenAPI description.
- The rule itself is applied using the `then` clause. In this example, the `security` property must be present on each resolved Operation, checked using the built-in function `truthy`.

The purpose of this ruleset - as the example shows - is to ensure that a Security Requirement is defined (although this does not check for an empty object, which is ignored to keep the example simple). This could be an important requirement for an API provider and therefore is implemented to check all designs include it.

When you apply it to this OpenAPI description:

```yaml
openapi: 3.1.0
info:
  title: Insecure example
  version: 1.0.0
paths:
  /insecure-endpoint:
    post:
      requestBody:
        description: Insecure
        content:
          application/json:
            schema:
              type: object
              additionalProperties: true
      responses:
        "201":
          description: Created
```

You get the following error:

```bash
(oai_course_chapter4) ➜  $ npx @stoplight/spectral-cli lint --ruleset ./insecure-endpoints-ruleset.yaml ./insecure-endpoints-openapi.yaml

./insecure-endpoints-openapi.yaml
  7:10  error  security-must-be-enforced-for-unsafe-endpoints        You need a Security Requirement for unsafe operations               paths./insecure-endpoint.post

✖ 1 problems (2 errors, 0 warnings, 0 infos, 0 hints)
(oai_course_chapter4) ➜  $
```

The elegance of this approach lies in how the ruleset can be applied. When developers create their OpenAPI descriptions they can automate their build pipeline to automatically execute the rulesets, ensuring they can tweak their design as expediently as possible. As we know from the general discourse across information technology, automation is highly valued and such approaches to testing for accuracy in API design can only be a boost for API providers.

### Task: Add Governance Rules to a Spectral Ruleset

Spectral is a **_hugely_** popular example of an API governance tool.

We've defined an example [Spectral ruleset](https://github.com/OAI/OAI-Courses/blob/main/chapter-4-examples/applying-governance/README.md) to help you understand more about this topic.

Please evaluate the examples and as a test of your knowledge add a rule that checks that all Schema objects implement the property `additionalProperties: false`. If this check fails an error message should be returned that reads "additionalProperties must be set to false in a Schema object".

When you have done this successfully the following errors will appear in the output from Spectral:

```bash
https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-v31-fundamentals/chapter-3-examples/design-first-example/design-first-example-openapi.yaml
   2:6   warning  info-contact                         Info object must have "contact" object.                                         info
  53:20    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    paths./pets.post.requestBody.content.application/json.schema
  104:9    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    components.schemas.Pet
 119:11    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    components.schemas.Error
```

Please also make sure you search the internet for alternative Spectral rulesets as there are hundreds of examples out there. Start with the list of real-world rulesets from the [Spectral documentation](https://docs.stoplight.io/docs/spectral/674b27b261c3c-overview#-real-world-rulesets).

## Knowledge Check

Congratulations on completing Chapter 4 - Using an OpenAPI description. Take this quiz to check your understanding of the concepts you've learned about so far.

### Question 1

Why is a lifecycle view of OpenAPI important?

- [ ] Helps you understand how to version APIs
- [ ] Helps you generate documentation
- [x] Helps you understand the use cases in which an OpenAPI description can be used
- [ ] None of the above

### Question 2

Why might an OpenAPI description be used to generate documentation?

- [x] Provides the means for human beings to easily understand the structure of the API
- [ ] Allows the documentation to be screen-scraped by tooling
- [ ] Provides neat widgets that can be embedded in websites
- [ ] It isn't a valid approach because an OpenAPI description is encoded in JSON or YAML

### Question 3

What makes OpenAPI descriptions a rich source of information for generating documentation?

- [ ] The use of JSON or YAML to encode the document
- [x] The ability to include Markdown in the description
- [ ] Tooling vendors and the quality of their graphics
- [ ] None of the above

### Question 4

What is the goal of generating an API client from an OpenAPI description?

- [ ] Repeatability
- [ ] Efficiency
- [ ] Accuracy
- [x] All of the above

### Question 5

What programming languages can API clients be generated in?

- [ ] Python
- [ ] Java
- [ ] Lisp
- [x] Anywhere tools are available in the ecosystem

### Question 6

What other example did we give of how an OpenAPI description can be used by API consumers?

- [x] Configuring infrastructure such as API gateways
- [ ] Generating keys and certificates
- [ ] Writing Gherkin-style test cases
- [ ] Testing requirements

### Question 7

In this example, what did we point to as being a common way of extending OpenAPI descriptions to provide additional information?

- [ ] Comments
- [ ] Overlays
- [x] Specification Extensions
- [ ] Descriptions

### Question 8

Can tools like Spectral meet all your API governance needs?

- [ ] Yes, they are a silver bullet
- [ ] No, you need other tools to test the API design
- [ ] No, you need to test the implementation in your software
- [x] No, you need to test both the design and the implementation with the appropriate tools

### Question 9

How is an object matched to a rule in a Spectral ruleset?

- [ ] XPath
- [ ] JSON Pointer
- [x] JSON Path
- [ ] Line and column numbers

### Question 10

How do tools like Spectral provide a boost for API governance in organizations

- [ ] Provides a quality gate in a governance process
- [ ] Allows API design to be completed consistently
- [ ] Allows standards to be applied to design
- [x] All of the above
