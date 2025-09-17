# Using an OpenAPI Description

## Introduction

### Chapter Overview

OpenAPI descriptions created by API providers can be used by both API consumers and the API provider themselves in many different ways. Many of the ways in which an OpenAPI description can be used can be qualified in the stages of the API lifecycle. This concept was introduced in the chapter "_Creating an OpenAPI Description_."

API providers and consumers can use an OpenAPI description for various purposes, such as generating documentation, creating an API client, applying governance to API design, and many other activities. These activities help API consumers to perform their roles more accurately and efficiently.

### Learning Objectives

By the end of the chapter you should be able to:

- Discuss how OpenAPI supports activities of an API lifecycle

- Evaluate how OpenAPI is applied based on several use cases and examples

- Use OpenAPI in your organization's API lifecycle

## Using an OpenAPI Description and the API Lifecycle

### The API Lifecycle

In the chapter _Creating an OpenAPI Description_ we introduced a hypothetical API lifecycle. This lifecycle was created by the OpenAPI Initiative to explain how OpenAPI can be used throughout the development and deployment of APIs:

![The API lifecycle as imagined by OpenAPI Initiative](https://www.openapis.org/wp-content/uploads/sites/3/2023/05/What-is-OpenAPI-Simple-API-Lifecycle-Vertical.png)

**The API lifecycle as imagined by OpenAPI Initiative\
_Source: [OpenAPI Initiative](https://www.openapis.org/)_**

Each stage in this lifecycle is associated with different organizational roles, with a variety of wants and needs from the people partaking in each stage. The wants and needs of those individuals determine a significant number of use cases for API-related documentation driven by those activities. Some of these use cases may already be familiar to you, while others may be novel in terms of your experiences with APIs. We will look at several common use cases and provide examples of toolsets that show how an OpenAPI description is leveraged to fulfill the use cases.

Please note that, being an open format, OpenAPI can be used in a huge number of ways depending on the perspective of the API consumer, specific developers, and tooling makers. We are only covering very common activities here.

## Generating API Documentation

### Use Case for Generating API Documentation

Our first use case is generating documentation, a feature of the Publish stage of an API lifecycle. You might question why this is the case, given that an OpenAPI description is a document encoded in JSON or YAML with a specific structure.

Even the bare minimum of information in an OpenAPI description tells us something about the shape of an API. However, the inclusion of Markdown in the specification means that **description** properties can be very rich, including formatting and links to graphics. An OpenAPI description can provide the spine of the documentation, with Markdown content providing the \"meat on the bone\". Therefore, toolsets have evolved that use the content of the OpenAPI description to drive the rendering of human-oriented documentation built for browsing the operations the API supports.

### Example of Generating API Documentation

You can understand how rich this documentation can be by looking at some examples in the wild. Take, for example, the organization Zuora, which provides documentation using Redoc. Their [API documentation](https://developer.zuora.com/api-references/api/overview/) is comprehensive, providing developers with everything they need to know about the operations the API supports. Only some of the content is embedded in the OpenAPI description as it is too voluminous to manage there, but the structure ties the information together. OpenAPI provides the skeleton, which is merged with other documentation sources through automation and a "[DocOps](https://www.writethedocs.org/guide/doc-ops/)" lifecycle before publication.

### Task: Generate API Documentation Using Redoc

Redoc is an open source tool we mentioned in a previous chapter. It is an easy way to provide an example of generating documentation, as shown in the screenshot below:

![An example of an Info Object rendered with Redoc](images/redoc-example.png)

**_An Example of an Info Object Rendered with Redoc_**

If you want to explore publishing documentation in more detail, follow [the example](https://github.com/lftraining/LFELL1011-resources/tree/main/chapter-5-examples/generating-documentation#readme) of using Redoc with our [design-first OpenAPI description](https://github.com/lftraining/LFELL1011-resources/blob/main/chapter-4-examples/design-first-example/design-first-example-openapi.yaml). The README in the repository provides full instructions on how to get up and running with the open source version of Redoc.

## Generating an API Client

### Use Case for Generating an API Client

Our first use case showed how API providers can consume their own OpenAPI descriptions for tasks like publishing API documentation. It makes sense, however, for API providers to also publish OpenAPI descriptions directly to API consumers so that they can use it in whatever way they see fit. Human-focused documentation is only part of what API consumers need --- they also want the descriptions to be compatible with tools that understand OpenAPI and assist them in working with APIs. Publishing OpenAPI description to the developer community is an absolute must for API providers, as it helps drive the consumer side of the API lifecycle and gives API consumers autonomy in how they execute their lifecycle and what tools they choose to use.

Providing an OpenAPI description is, therefore, one of the main activities of the Publish stage in our lifecycle. API providers will publish an OpenAPI description document, encoded in either JSON or YAML, through their developer portal that API consumers can download or reference. From there consumers can use the OpenAPI description to generate code, create test cases, or configure their infrastructure.

One example of how an OpenAPI description can be used by both an API provider and an API consumer is to create software clients that reflect the API's structure, security, parameters, requests, and responses. Creating a client for communication with external services is a very common pattern in software development, and APIs are no exception to this pattern. API providers often provide client software to their developer community as Software Development Kits (SDKs). The client is used as a consistent way to invoke the API, providing a standardized mechanism that precisely reflects the description of the API. The client performs many functions, such as parameter injection, security credential injection, and payload validation.

Creating a software client is usually done by processing the description and performing code generation in the target language of your software application. There are an **_enormous_** number of tools that will generate client code or SDKs for you (with the name depending on whether you are an API consumer or API provider) with your choice of tool based on the support available for your programming language or application framework.

### Example of Generating an API Client

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

The developer uses the **ApiClient** object to interact with the API, simplifying the integration effort. This example is simple and can also be achieved with many other toolsets. The point is, however, that it meets the goal of seamlessly passing knowledge from the API provider to API consumers, who can use that knowledge in as near automated fashion as possible. A significant boost can be provided for developers who do not need to handcraft a client to access a given API.

We've picked generating an API client as a use case, which can be useful for both API consumers and API providers, but you can extend the scope of this example back into the Configure stage of our API lifecycle in the role of an API provider. Many tooling vendors, especially those in the API management space, leverage OpenAPI descriptions to configure infrastructure such as API gateways. Typically, these will be enhanced with Specification Extensions, which we will cover in the next chapter.

### Task: Generating an API Client using Kiota

Kiota supports a number of programming languages.

Use one of the [quick-start guides](https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/) in your choice of programming language to explore generating an API client in more detail.

Use our [design-first OpenAPI description](https://github.com/lftraining/LFELL1011-resources/blob/main/chapter-4-examples/design-first-example/design-first-example-openapi.yaml) as an input to your API client.

## Applying Governance

### Use Case for Applying Governance

In our first two use cases we've focused largely on meeting the needs of API consumers by providing an OpenAPI description to help with the goal of integrating with your APIs. There are other ways we can leverage our OpenAPI description before publishing it to API consumers or using it to publish documentation or SDKs that the API consumer needs. One area is that of ensuring our APIs adhere to our internal standards for design, which is often called **_design-time governance_**. This style of governance is an essential part of the API lifecycle in many organizations. It ensures that when published to consumers, APIs are designed to be consistent and fit for purpose.

Design-time governance is also useful as it can help catch issues where your API design does not meet your organization's API standards. Of course, you need to create or generate your OpenAPI descriptions early enough in the API lifecycle to succeed in this style of governance, but it can reap rewards for your organization.

### Example of Applying Governance

One example of a tool that can help you apply design-time governance is [Spectral](https://stoplight.io/open-source/spectral), which uses style guides codified as \"rulesets\" to work as a design linter, i.e. as a tool that provides feedback about your design's adherence to certain rules. Spectral is an open source command-line tool and can be deployed virtually anywhere.

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

- The ruleset extends Spectral's default ruleset for OpenAPI (**extends: spectral:oas**).

- The **rules** property allows you to specify one or more design rules with each uniquely identified with a name.

- Each rule provides a message and severity to drive how to correct behaviors when an error is encountered.

- A JSON Path is specified to indicate the object to which the rule applies in an OpenAPI description.

- The rule itself is applied using the **then** clause. In this example, the **security** property must be present on each resolved Operation, checked using the built-in function **truthy**.

The purpose of this ruleset is to ensure that a Security Requirement is defined (although this does not check for an empty object, which is ignored to keep the example simple). This ruleset could be an important requirement for an API provider and therefore is implemented to check that all designs include it.

When you apply the ruleset to this OpenAPI description:

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

**(oai_course_chapter4) ➜ \$ npx \@stoplight/spectral-cli lint \--ruleset ./insecure-endpoints-ruleset.yaml ./insecure-endpoints-openapi.yaml\
\
./insecure-endpoints-openapi.yaml\
7:10 error security-must-be-enforced-for-unsafe-endpoints You need a Security Requirement for unsafe operations paths./insecure-endpoint.post\
\
✖ 1 problems (2 errors, 0 warnings, 0 infos, 0 hints)\
(oai_course_chapter4) ➜ \$**

The elegance of this approach lies in how rulesets can be applied. When developers create their OpenAPI descriptions they can automate their build pipeline to automatically execute the rulesets, ensuring they can tweak their design as expediently as possible. As we know from the general discourse across information technology, automation is highly valued and such approaches to testing for accuracy in API design can only be a boost for API providers.

### Task: Add Governance Rules to a Spectral Ruleset

Spectral is an **_extremely_** popular example of an API governance tool. It's worthwhile mentioning that Spectral comes with built-in rules that already help you to improve the quality of your OpenAPI descriptions. However, many Spectral users go beyond this simple usage and start writing their own rulesets to represent their own guidelines for OpenAPI descriptions.

We've defined an example [Spectral ruleset](https://github.com/lftraining/LFELL1011-resources/blob/main/chapter-5-examples/applying-governance/rulesets/baseline.yaml) to help you understand more about this topic.

Let's test your knowledge. Please refer to the [README](https://github.com/lftraining/LFELL1011-resources/blob/main/chapter-5-examples/applying-governance/README.md) in our example repository for instructions on getting set up with Spectral. Then evaluate the examples and add a rule that checks that all Schema objects implement the property **additionalProperties: false**. If this check fails, an error message should be returned that reads \"additionalProperties must be set to false in a Schema object\".

When you have done this successfully the following errors will appear in the output from Spectral:

```bash
https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-fundamentals/v31/chapter-3-examples/design-first-example/design-first-example-openapi.yaml
   2:6   warning  info-contact                         Info object must have "contact" object.                                         info
  53:20    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    paths./pets.post.requestBody.content.application/json.schema
  104:9    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    components.schemas.Pet
 119:11    error  additional-properties-must-be-false  additionalProperties must be set to false in a Schema object                    components.schemas.Error
```

Please also make sure you search the internet for alternative Spectral rulesets as there are hundreds of examples out there. Start with the list of real-world rulesets from the [Spectral documentation](https://docs.stoplight.io/docs/spectral/674b27b261c3c-overview#-real-world-rulesets).

## Knowledge Check

Congratulations on completing Chapter 5 - Using an OpenAPI description. Take this quiz to check your understanding of the concepts you've learned about so far.

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

What makes OpenAPI descriptions a rich source of information for generating human-facing documentation?

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

- [x] Any language for which tools are available in the ecosystem

### Question 6

Which of the following activities can be completed using an OpenAPI description?

- [x] Configuring infrastructure such as API gateways

- [ ] Generating keys and certificates

- [ ] Writing Gherkin-style test cases

- [ ] Testing business requirements have been delivered

### Question 7

What is a common way of extending OpenAPI descriptions to provide additional information?

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

How do tools like Spectral provide a boost for API governance in organizations?

- [ ] Provides a quality gate in a governance process

- [ ] Allows API design to be completed consistently

- [ ] Allows standards to be applied to design

- [x] All of the above
