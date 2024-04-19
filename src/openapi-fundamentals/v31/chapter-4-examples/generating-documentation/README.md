# Generating API documentation using OpenAPI and Redoc

This project is a very simple example of rendering documentation using an API description and Redoc.

## Dependencies

You need Python 3 available to run this example.

## Running It

Do as follows:

- Change to this directory
- Execute `python -m http.server`
- Open your browser at http://localhost:8000

You'll see the OpenAPI description we introduced in Chapter 3 rendered as an HTML page.

:thumbsup:

## Explanation

Redoc is - amongst other things - a JavaScript library that provides a visual wrapper around OpenAPI.

The file [index.html](index.html) implements an element `redoc` that references the URL of the input OpenAPI specification in the argument `spec-url`.

This is rendered by the Redoc package as it expects the `redoc` element to be an argument to its rendering function. The package is referenced from a CDN using a standard `script` element.
