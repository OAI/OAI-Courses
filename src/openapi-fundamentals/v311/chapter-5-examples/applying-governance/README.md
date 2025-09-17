# Applying Governance with Spectral

This project is a very simple example of applying governance to an OpenAPI description using Spectral.

## Dependencies

You'll need a recent version of Node.js available. Once you have this (ideally use `nvm` to get it), install the Spectral CLI using `npm` or your package manager of choice:

```bash
npm install --global @stoplight/spectral-cli
```

The Spectral CLI should now be in your path ready to use.

## Running It

To run our baseline Spectral ruleset against the OpenAPI description from Chapter 3 execute the following command in this directory:

```bash
spectral lint --ruleset rulesets/baseline.yaml https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-fundamentals/v31/module-3-examples/design-first-example/design-first-example-openapi.yaml
```

You should see the following output:

```bash
https://raw.githubusercontent.com/OAI/OAI-Courses/main/src/openapi-fundamentals/v31/module-3-examples/design-first-example/design-first-example-openapi.yaml
  2:6  warning  info-contact      Info object must have "contact" object.                                         info

✖ 2 problems (0 error, 1 warnings, 0 infos, 0 hints)
```

## Task

If you are tackling the task from Chapter 3 here are a few hints on building your rule:

- You'll need to find everything in the OpenAPI description that looks like a Schema object.
- You should filter for anything where `additionalProperties: false` is already set.
- You should provide an appropriate error message to indicate the issue.

Please visit the Spectral documentation [page](https://docs.stoplight.io/docs/spectral) for more detailed information on how Spectral works.
