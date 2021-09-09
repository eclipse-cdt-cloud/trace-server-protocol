# trace-server-protocol

Specification of the Trace Server Protocol

This protocol is built to decouple the backend and frontend of trace analysers, allowing traces to reside and be analysed on the backend, and visual models to be exchanged with a variety of clients.

The protocol is meant to be RESTful, over HTTP.

The specification is currently written in **OpenAPI 3.0** and can be pretty-visualized in the [github pages](https://theia-ide.github.io/trace-server-protocol/).

## HOW-TO

The specification should be edited with the [swagger editor](https://swagger.io/swagger-editor/) which also handles validating that the OpenAPI specification is respected.

Another option is the [OpenAPI (Swagger) Editor extension](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi) for VS Code.

The latter extension is assumed for consistent formatting of the `./API.yaml` file over time.
