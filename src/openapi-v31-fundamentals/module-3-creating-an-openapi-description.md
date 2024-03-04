# Creating an OpenAPI document

Welcome to our course module "Creating an OpenAPI document".

In Module 2 we described the basic structure of OpenAPI and how it reflects the structure and semantics of HTTP.

This module is where the "rubber hits the road" in using OpenAPI practically.

We look at:

- The different design methodologies, namely Design-first and Code-first.
- How to approach Design-first and an introduction to tools that can help you.
- Some basic examples of the Code-first methodology, using sample code in Java and Python.
- How to decide what best suits your needs based on who you are and what kind of organization you work for.

At the end of the module you'll be able to apply what you've learnt in practical situations when you create APIs.

In this module we'll also introduce some OpenAPI features we didn't go into in module 2. We introduce them here to ensure you have the best chance of creating rich OpenAPI documents once you've taken the course.

First up, lets look at the choice of design methodologies available to us in creating our OpenAPI documents.

## Design Methodologies: Code-first vs. Design-first

Design methodologies in the creation of APIs have grown organically and are fundamentally tied to both tooling and the how orientated designers are towards writing software. The approaches are generalised into two mainstream methodologies:

- **Design-first**: You start with the specification - written (for the sake of this course) in OpenAPI - that is based on your wants and needs as the creator of the API. You draw out the required Paths, Path Items, Operations and Schema objects you need. You then use this document for creating your implementation in code, plus other activities like generating documentation and setting up test cases.
- **Code-first**: You start writing your implementation code and use this to drive the shape of the API. You either build the structure of your API from scratch or use a framework of choice. You then annotate your code and generate an OpenAPI document based on the shape of the implementation code.

We'll start by looking at design-first, as this is arguably the most simple to get going with (from the perspective of reinforcing some points about OpenAPI) and therefore a good way of drawing out some examples.

## Using Design-first

Design-first is an attractive approach to creating APIs because you see you results instantly, and can therefore readily understand the shape of your API. This might seem like a simple point, but it opens up creating APIs to a whole bunch of people who **_don't_** cut code: product managers, architects and so on. This especially important in areas like the development of market standards because developers aren't always responsible for the shape of an API, and that shape can have many stakeholders.

The approach is also simple from a tooling perspective. You can use a text editor and your knowledge of OpenAPI to create a specification. However, there is myriad of editing tools available - some text-based, some graphical - that can help you create an OpenAPI document from scratch.

To provide an example we'll be use a text editor that allows you shape your API design but also offers a graphical view of your API as you design it. That view is not the only way that an API can be visualized, but it is a good place to get started as you'll see the structure of the OpenAPI document as you create it.

### Creating an OpenAPI document in Swagger Editor

To show how design-first works we are using Swagger Editor, which is arguably the most freely-available editing tool for OpenAPI. Despite its name - Swagger being a reference to the pre-OpenAPI name of the specification - the latest version of Swagger Editor supports all versions include 3.1. Getting started is as easy as going to the [right URL](https://editor-next.swagger.io/).

When you get there for the first time you'll see the default, expanded version of the Petstore API:

![Petstore API Screenshot](images/swagger-editor-screenshot.png)

You can clear the pane on the left-hand side and the rendered view of the API will be removed.

Starting with a blank canvas is often a good way to start as it makes you think about the way an API is structured with an open mind. You can use your editor as a notebook, getting the most important "facts" about your API into place before assessing what the finer details need to look like.

To turn the blank view of your API into something, copy-and-paste the follow snippet into the editor:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
paths:
  /pets:
    get:
      responses:
        "200":
          description: OK
```

This is about as minimal an API specification as you can get (although admittedly you could have an empty Paths object, but that doesn't help us much).

It obviously isn't very informative, but gets the very basics of a valid structure namely:

- You have provided a title and version.
- A `get` operation hosted at the URI `/pets`.
- Requesting this endpoint will return a HTTP 200 response code.

This, however, in insufficient for an API consumer. We don't tell them anything about parameters, HTTP headers or shape of the request or response bodies. The next most useful we can add here is a representation of the response body using a Schema object, which tells our API consumers what the properties of a pet are.

This can be declared inline if desired, encapsulated in a Content and Media Type object to indicate that a JSON response body is supported:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
paths:
  /pets:
    get:
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: array
                maxItems: 100
                items:
                  type: object
                  required:
                    - id
                    - name
                  properties:
                    id:
                      type: integer
                      format: int64
                    name:
                      type: string
                    tag:
                      type: string
```

We know now this operation will return a response body encoded in JSON with a root array of up to 100 pets. However, declaring the properties of the pet inline is probably not what we want to do as we might want to reuse the object.

We therefore move that to the Components Object inside the `schemas` property and use a Reference Object to point to it:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
paths:
  /pets:
    get:
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: array
                maxItems: 100
                items:
                  $ref: "#/components/schemas/Pet"
components:
  schemas:
    type: object
    required:
      - id
      - name
    properties:
      id:
        type: integer
        format: int64
      name:
        type: string
      tag:
        type: string
```

In doing this we're already set-up to make our OpenAPI document more concise because we've set up the Pet property for reuse.

We can do the same when we design for returning HTTP errors:

```yaml
openapi: 3.1.0
info:
  title: OpenAPI v3.1 Fundamentals API
  description: A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course.
  version: 1.0.0
paths:
  /pets:
    get:
      responses:
        "200":
          summary: List of pets
          description: List of pets provided at the Petstore
          content:
            application/json:
              schema:
                type: array
                maxItems: 100
                items:
                  $ref: "#/components/schemas/Pet"
        default:
          description: Non-specific HTTP response code
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
components:
  schemas:
    Pet:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: integer
          format: int64
        name:
          type: string
        tag:
          type: string
    Error:
      type: object
      required:
        - code
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
```

In this iteration we've used the `default` property rather than specific return codes, as this allows us to provide a catchall for anything else returned. Note also that the `integer` properties are qualified with the `format` property, indicating whether the values are signed or unsigned. Providing such information is one of the key features of OpenAPI, in that we are providing useful information to consumers of APIs upfront, so their reflect it in their implementation code.

The next step - although optional - is to add some tags. The [Tag Object](https://spec.openapis.org/oas/v3.1.0.html#tag-object) helps API providers classify their Path Items for users so that can more readily navigate the available Operations. Adding one-or-more tags to an Operation means adding a property called `tags`, which is an array:

```yaml
paths:
  /pets:
    tags:
      - GET
      - Read One-or-more Pets
    get:
      responses:
        "200":
        ...
```

You can also add a root-level Tags object that facilitates rendering Tag objects with a description:

```yaml
tags:
  - name: GET
    description: HTTP GET operations
  - name: Read Pets
    description: Retrieve the properties of one-or-more pets based on the requested URI
```

[Redoc](https://github.com/Redocly/redoc) provides an example of how tags are used in rendering the display shown below.

The tags drive the navigation menu on the left-hand side, with the API provider responsible for providing meaningful data so the navigation menu is helpful to the API consumer:

![Redoc Navigation Example](images/redoc-screenshot.png)

<blockquote>
The tags here are used as an example and the way they are structured - so that multiple tags reference a single endpoint - is not the best way of tagging.

However, it serves as an example as some tooling makers might support such tagging in a useful way.

</blockquote>

To complete our basic example we need some security information that lets our API consumers know what secures the API. In the case of the example we are using API keys, which we define using a [Security Scheme object](https://spec.openapis.org/oas/v3.1.0.html#security-scheme-object):

```yaml
components:
  securitySchemes:
    apiKey:
      description: API key as provided in Petstore portal
      type: apiKey
      in: header
      name: api-key
```

This specifies an API key that is sent using a HTTP header called `api-key`. We can add this to the document root as a global [Security Requirement](https://spec.openapis.org/oas/v3.1.0.html#security-requirement-object) so it applies to all Operations:

```yaml
security:
  - apiKey: []
```

> To understand the empty array shown in the example please refer to our security section in Module 2.

Another piece of information we could add is a [Servers Object](https://spec.openapis.org/oas/v3.1.0.html#server-object) that provides a list of URLs that the API is accessible, a description of the instance and a mapping of variables to a given value (for example, defining the port the API is published on). As we are doing design-first and don't know anything about the deployment, however, we aren't adding this here. We'll see a server variable when we look at the code-first example.

We've therefore built a very simple OpenAPI document from nothing into something that provides enough information for an API consumer to get working with our API and - in the case of so many organization - provide information for testers, technical writers, and other users of the OpenAPI document.

We've not used anything other than a text editor to do this, but it gives so many consumers of this information a starting point for their work, plus a means to readily test that the API is designed to requirements and can be immediately compared to internal API standards.

Or course, this approach is not for everyone. Lets look at how we can get to this same point in our design using a code-first approach.

<blockquote>
Before you go on, load the [complete design-first example](src/openapi-v31-fundamentals/module-3-examples/design-first-redoc-example/design-first-example-openapi.yaml) into Swagger Editor so you can review all the Operations supported by the API.

Please note:

- There are Operations to both create a pet and retrieve the properties of a pet using the identifier `petId`.
- These Operations implement Reference Objects as we described above to reuse existing definitions.
- The security model is inherited from the global Security Requirement, so no Security Requirements are found on any operation.

Reviewing the OpenAPI document as it stands will be useful when you look at the code-first approach below.

</blockquote>

## Using Code-first

Design-first obviously has some benefits for rapid prototyping and shaping ideas.

However, code-first is probably most mature of the two design methodologies discussed in this module. The reason for this is quite simple, namely: Implementation code predated API specification languages, which in turn were born from the need to produce a schematic representation of an API for consumption outside the code base. This has long been a need in the API economy, and in software engineering in general. We cannot simply throw open out code repositories and invite any external collaborators in to view our implementation code. We need the means to provide this outside our safe and secure codebase.

That fact is true regardless of whether we are going with code-first or design-first, but it's all the more pertinent in the code-first world. The reason that API specification languages came into being is so developers could automatically generate API-related documentation based on the shape of their implementation code.

The methodology is generally as follows:

1. Write implementation code that reflects a given request or response.
2. Implement routing to provide request and response operations.
3. Apply meaningful annotations that can transpose the "shape" of the code to an API description document.
4. Generate the API description document at build time, source control it and distribute the document to interested parties.

This approach has grown organically and matured over time, and is not unique to OpenAPI. There is also a huge number of packages that support code-first.

We have two examples in the sections below that use springdoc-openapi and APIFlask, written in Java and Python respectively, to demonstrate how code-first works with popular programming languages and frameworks.

In both examples we'll use uses the stripped-down Petstore API we created in the design-first section as the implementation requirement, and show how this OpenAPI description would be generated from code.

### Code-first Example: springdoc-openapi

[springdoc-openapi](https://springdoc.org/) is a library designed for [Spring Boot](https://spring.io/projects/spring-boot) applications, a popular Java library with built-in support for building APIs.

[Our example](module-3-examples/code-first-using-springdoc-openapi/) is a **_very basic_** Spring Boot application that serves to demonstrate the annotations available with [springdoc-openapi](https://springdoc.org/). springdoc-openapi provides an introspection mechanism for Spring Boot web application that serves as the starting point for building an OpenAPI description. It then leverages swagger.io packages to provide additional annotations.

The project was initialized using the Spring Boot CLI and follows typical boilerplate commonly found in API-related projects. The example [README](module-3-examples/code-first-using-springdoc/README.md) provides details on getting this example up-and-running.

<blockquote>
Please note there almost zero complexity in this or the Python-based example - no unit tests, backend, external services, nothing - and this is for good reason.

The idea is to show how to generate an OpenAPI description using a code-first methodology, not to build a fully-featured API in Java. We give enough indicators in the description below to describe what's going on, but not a full digest of the code base itself.

We also **do not** provide instructions on exposing the OpenAPI description through Swagger UI, Redoc, _et al_. This style of tutorial is freely available on the internet. The point of this example is simply to provide more context on the decision you make to go with a code-first methodology.

</blockquote>

Walking through the example in code and using the design-first section as our reference, first off we need to provide an Info object that tells consumers of our OpenAPI document about the API: The title, version, description plus any other relevant information we can provide in the document Info object.

In the example we've defined a [separate class](module-3-examples/code-first-using-springdoc-openapi/src/main/java/org/openapis/first/code/config/CodeFirstConfig.java) to encapsulate this information, using application configuration as well to create the Info object:

```java
@Bean
public OpenAPI customOpenAPI(@Value("${application-description}") String appDesciption,
    @Value("${application-version}") String appVersion) {
  return new OpenAPI()
      .info(new Info()
          .title("OpenAPI v3.1 Fundamentals Example")
          .version(appVersion)
          .description(appDesciption));
}
```

Next we define the contents of our Paths object, which specifies the URIs by which each Operation - the combination of URI and HTTP method are available.

This is done in our example using the Spring Boot `@GetProperty` and `@PostProperty` annotations - as this is what our API implements - together with annotations that provide both `summary` and `description` properties for the Path Items in our API. springdoc-openapi combines this information to produce the OpenAPI description.

The encoding of the request and response payloads is also qualified using the `MediaType` class, which uses the constant `APPLICATION_JSON_VALUE` to indicate the `Content-type` header will be set to `application/json`. This will be reflected in the OpenAPI document:

```java
@Operation(summary = "Get pet by ID", description = "Retrieve a pet by its ID", operationId = "getPetById", responses = {
    @ApiResponse(description = "Pet found", responseCode = "200", content = @Content(schema = @Schema(implementation = Pet.class))),
    @ApiResponse(responseCode = "default", content = @Content(schema = @Schema(implementation = Error.class)))
})
@GetMapping(path = "/pets/{petId}", produces = { MediaType.APPLICATION_JSON_VALUE })
@ResponseBody
public ResponseEntity<?> getPetById(@PathVariable Integer petId) {
  Pet pet = allPetsMap.get(petId);
  if (pet == null) {
    Error errorResponse = new Error(1000, "Unknown Pet identifier");
    return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
  }
  return ResponseEntity.ok().body(pet);
}
```

Now is good time to compare the code with the OpenAPI document that is generated. If you followed the set-up instructions you should be able to run the `generateOpenApiDocs` Gradle command to generate a fresh copy of the OpenAPI document.

You'll note that the OpenAPI document you've generated includes a `servers` property, with the value of your local instance provided by springdoc-openapi. This may appear useful at first glance, but most likely you are going to want to include other values in this property, some of which you are not in control of or do not know. This is repeated theme in the OpenAPI world. A given OpenAPI description represents the shape and configuration of an API at a point in time, but generally speaking there is information outside the development team that will need to be added later in the API lifecycle.

The code-first world includes many examples like this - regardless of the programming language and application development framework - where the tooling maker makes a judgment about what is useful for the API provider but cannot foresee the OpenAPI document will be used in practicality. The impact of such decisions will become more obvious in our Using an OpenAPI description module when we look at the OpenAPI from an API consumers viewpoint.

### Code-first Example: APIFlask

Code-first is obviously an option in virtually any programming language and different approaches abound. For our Python example we use [APIFlask](https://github.com/apiflask/apiflask), a library that provides a wrapper on the very popular [Flask](https://flask.palletsprojects.com/en/3.0.x/) framework that brings OpenAPI functionality.

Like the springdoc-openapi project, [our example](module-3-examples/code-first-using-flask-openapi3/) is a very basic application that demonstrates using APIFlask to add OpenAPI annotations to the API.

<blockquote>
In this example we use the very bear minimum from APIFlask, in order to keep as close to a native Flask application as possible.

It also purposefully takes few shortcuts in the application, in order to demonstrate specific features of the code-first approach. Experienced API developers would almost certainly improve and simplify this codebase.

</blockquote>

Walking through the example in the same way we did with the Spring Boot application, the APIFlask object is created first in the same way as a regular Flask application. APIFlask includes arguments that provide the title of our API and version, and we can also update the description and OpenAPI version to provide the basis of the OpenAPI description we'll generate:

```python
# Application config including OpenAPI version, title, description and API version
app = APIFlask(
    __name__,
    title="OpenAPI v3.1 Fundamentals Example",
    version="1.0.0",
)
app.config["DESCRIPTION"] = (
    "A stripped-down version of the Petstore API for the OpenAPI v3.1 Fundamentals course."
)
app.config["OPENAPI_VERSION"] = "3.1.0"
```

This provides the API consumer with the high-level information on the API. Each route is then annotated using the `doc` decorator, which is populated with the `operationId`, tags and any other information. In this case APIFlask also allows the `default` responses we created in the design-first OpenAPI description to be associated with route, meaning it is pulled into the output document.

The example below shows the `post` Operation on the Path Item `pets`:

```python
@app.post("/pets")
@app.doc(
    operation_id="CreatePet",
    tags=["POST", "Create a Pet"],
    responses=default_responses_schema,
)
@app.input(PetProperties.Schema)
@app.output(EmptySchema, status_code=201)
def post_pets(json_data):
    """Create a new Pet

    Add a new Pet to the collection of pets at the Petstore API
    """

    global LAST_PET_ID
    global PETS

    # Belt-and-braces check but probably not necessary
    if json_data.name is None:
        raise MissingRequestProperty

    LAST_PET_ID = LAST_PET_ID + 1
    new_pet = Pet(LAST_PET_ID, json_data.name, json_data.tag)
    PETS[LAST_PET_ID] = new_pet

    return make_response("", 201)
```

The example also shows that the request and response payload representation can be bound to specific classes using the `input` and `output` decorators. These can bound to specific classes, with the request payload being bound in this case to the [`PetProperties` class](module-3-examples/code-first-using-apiflask/pet_properties.py). In this class we provided annotations that provide description of each property in our OpenAPI description:

```python
from dataclasses import field
from apiflask import Schema
from marshmallow_dataclass import dataclass


@dataclass
class PetProperties(Schema):
    """Attributes of a Pet that can be added to the Petstore"""

    name: str = field(metadata={"description": "Name of the pet", "required": True})
    tag: str = field(metadata={"description": "Pet category", "required": False})
```

## Tasks

We've walked through the design-first approach and code-first approach using frameworks in both Java and Python.

You should take time to explore these examples in more detail and, if you are a developer or simply interested in understanding more about the nuts-and-bolts of OpenAPI, make changes to the code samples that affect the shape of the OpenAPI document that are generated.

As an addendum to this exploration, here are some more targeted tasks you can undertake. We use excerpts of an OpenAPI document to set the requirement.

### Delete a Pet resource

Most APIs that allow you create a resource also provide the means to delete them.

Amend your API to provide a delete endpoint and annotate it so the following snippet of OpenAPI is matched (with the correct indentation in the generated OpenAPI document):

```yaml
delete:
  summary: Delete a Pet
  description: Delete a Pet resource using the petId
  operationId: DeletePet
  responses:
    "204":
      description: Pet deleted
    default:
      content:
        application/json:
          schema:
            $ref: "#/components/schemas/Error"
```

Note the absence of a response body in the requirement. The 204 response code indicates no content is returned meaning there is no requirement to include a definition in the OpenAPI document.

### Add a Tag

The tags we've provided in our design can be changed in any manner you see fit. Add a tag that allows the delete operation above to be classified with the tag "HTTP DELETE Operations" and provide a suitable description.

### Add a Link

We've not touched on the [Link Object](https://spec.openapis.org/oas/v3.1.0.html#link-object) yet but this is a way to provide information to relate one request to another. OpenAPI provides this as a way of providing this information deterministically and at design time so that consumers of your API can understand it and accommodate it in their client.

Take the following simple example:

```yaml
responses:
  "201":
    description: OK
    content:
      application/json:
        schema:
          type: object
          required:
            - petId
          properties:
            petId:
              type: string
    links:
      GetDetailsOfPet:
        operationId: getPet
        parameters:
          petId: $response.body#/petId
```

What this example says is:

- When a 201 return code is returned I am providing a relationship between two Operations based on the object GetDetailsOfPet.
- The target operation has the `operationId` value of `getPet`.
- You can use the value of `petId` returned in the response body to set the `petId` parameter for the `getPet` operation.

This simple example shows how powerful the information contained in a Link Object can be. Take time to replicate this in the Java or Python codebase (You'll need to do the research to find out how to do it).

## What approach fits your needs?

You choice on adopting Code-first or API-first design - or maybe both, on a project-by-project basis - rests on a number of factors.

First off, who are you and what role do you play? This can often be the most important factor in deciding on a particular methodology. If you're a developer you may feel that its code-first and nothing else; you are in charge of the shape of the API, and the easiest way of ensuring that it by tieing it to the code base as closely as possible.

If, however, you are not a developer but in charge of setting the requirements for software development teams you may feel that design-first really suits your needs. You can sketch out the shape of the API using an OpenAPI description, supported by tooling, and use this as version 0.1.0 of the API, which is then implemented in code. This is especially attractive for you because you pull on industry standards - with pre-canned Schema Objects in either OpenAPI or JSON Schema - to create your request and response payloads.

In truth in most organizations there is no binary choice between the code-first and design-first methodologies. They'll be cases where it makes sense to generate OpenAPI descriptions from code, whilst in others there's motivation to do design upfront due to specific product team requirements that influence the shape of the API. It's also worth thinking about the approach by asking yourself a few questions:

- Is the code base the best place place to deal with tags and their descriptions?
- If you need to change the description of an Operation or Schema Object property is it easy for someone with responsibility to do this?
- If it easy to change information that it altered when an instance of the API is deployed?

The answers to those questions are likely to indicate a mix of responses that in some cases favour design-first and in others code-first. Many organisations actually opt for a hybrid approach, where code-first allows the shape of the API to be driven close to code base, ensuring the interface and the implementation stay in sync. Alongside this the principles of design-first enables copywriting teams to add suitable descriptions and information outside the code delivery mechanisms, embellishing the shape of the API with information suitable for display and therefore digestion by humans. This approach also allows API governance to be applied outside the code base, with activities such as standards compliance and versioning being orchestrated away from source control. Think of our code-first examples; if you are developer, would it practical for you or a technical writer to maintain all the descriptions in your code base?

Your efforts and how to take the right approach therefore ideally needs to be couched in how you approach the lifecycle of your APIs.

Take the following hypothetical API lifecycle as an example:

![OpenAPI API Lifecycle](https://www.openapis.org/wp-content/uploads/sites/3/2023/05/What-is-OpenAPI-Simple-API-Lifecycle-Vertical.png)

At each stage there is potentially a need to process a given OpenAPI document, with the wants-and-needs of the API consumer at that stage being different to what the developer adds to the codebase. An API provider needs to be cognizant of the varied audiences and their roles, and cater for how the deal with ensuring the information provided in a given OpenAPI document is as complete as it possibly can be. Most important in this is being aware of the fact that the development team is not necessarily the sole arbiter of the content of an OpenAPI document, and other contributors need to be enabled accordingly.

> We'll explore the idea of the API lifecycle more in Module 4. If you want to understand our API lifecycle model in brief then please read our article [What is OpenAPI](https://www.openapis.org/what-is-openapi).

The choice you make in terms of code-first verses design-first will there be influenced by many factors including who you are, what type of organization you work in who needs to consume your OpenAPI document. You should therefore invest time in assessing your wants-and-needs based on the details above, and make choices that given you the best chance of success.

## Plenary

Module 3 introduces the practical aspects of creating and publishing an OpenAPI description that describes our API. We've look at the two main methodologies, code-first and design-first, and discussed how each fits the needs of different roles in organization. To help bring the difference to life we've walked through design-first using Swagger Editor and two code-first examples in Java and Python.

This module has hopefully given us a solid grounding in the fundamentals of creating an OpenAPI description. In our next module we'll look at OpenAPI in the lense of the API consumer and understand how OpenAPI descriptions can be used effectively.

## Quiz

To help reinforce your knowledge please answer the following questions.

### Question 1

What are considered to be the two main methodologies for creating APIs?

- [ ] Requirements-first
- [x] Design-first
- [ ] Code-first
- [ ] All of the above

### Question 2

What is the bare minimum you need to create an OpenAPI description using design-first?

- [ ] An IDE installed
- [x] Knowledge of OpenAPI
- [x] A text editor
- [ ] None of the above

### Question 3

What's one of the ways that Tags can be used?

- [ ] Introduce a taxonomy of APIs in your organization
- [x] Provide the means to group Operations by a common coarse-grained identifier
- [ ] Allow attributes to be sent in your API request
- [ ] Specify additional metadata in your Schema object properties

### Question 4

What application framework is springdoc-openapi used with?

- [x] Spring Boot
- [ ] Struts
- [ ] Dagger
- [ ] Play

### Question 5

In both code-first examples how was the Info object set?

- [ ] Added manually after the OpenAPI description is generated
- [ ] Using arguments passed into the common-line tools
- [ ] By introspection
- [x] Using custom arguments or properties provide by the supporting packages

### Question 6

Name a side effect of using the code-first approach

- [ ] You can only update your OpenAPI description in your code base
- [x] Your OpenAPI description may contain additional information based on the tooling makers' opinion
- [ ] The encoding of your OpenAPI description may not be in JSON or YAML
- [ ] You make have to make compromises in the OpenAPI description you provide to API consumers

### Question 7

What is the `servers` property?

- [ ] A list of servers used in the development of your API
- [ ] A list of servers used in the test of your API
- [x] A list of deployed, available instances of the API described in an OpenAPI description
- [ ] A list of the most popular waiting staff in town

### Question 8

What is a Link Object?

- [x] A way of describing the link between two Operations in OpenAPI
- [ ] A URL that provides external documentation
- [ ] A URL that provides the terms and conditions of using the OpenAPI
- [ ] None of the above

### Question 9

How you should think about the API-related activities that occur in your organization?

- [ ] Using guidance provided by a project manager
- [ ] Using requirements set by your developer community
- [x] Using an API lifecycle to qualify how you perform those activities
- [ ] Look at that piecemeal as an unstructured approach works best

### Question 10

What is a valid consideration when choosing a design methodology

- [x] The means by which descriptions of operations and objects can be updated
- [ ] Your choice of programming language
- [ ] How many APIs you have
- [ ] The size of your organization
