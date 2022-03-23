# trace-server-protocol

Specification of the Trace Server Protocol

This protocol is built to decouple the backend and frontend of trace analysers, allowing traces to reside and be analysed on the backend, and visual models to be exchanged with a variety of clients.

The protocol is meant to be RESTful, over HTTP.

The specification is currently written in **OpenAPI 3.0** and can be pretty-visualized in the [github pages][tspGhPages].

## Current version

The current version of the specification is currently implemented and supported in the [Trace Compass trace-server][tcServer] (reference implementation) and what is currently supported by the [tsp-typescript-client][tspClient].

Swagger can be used to generate the API version implemented in Trace Compass trace-server (see [here](#generate-the-specification)).

## Future version

Some proposal for additional endpoints and features are documented in the `./API-proposed.yaml`. All the proposed changes are still not confirmed and can change. The pretty-visualized file can be found [here][apiProposed]. A diff of the current version and future version will show the differences.

Once an update has been approved it will be migrated to the main `./API.yaml` file.

## Update manually

The specification should be edited with the [OpenAPI (Swagger) Editor extension][vscodeOpenapi] for VS Code.

The latter extension is assumed for consistent formatting of the `./API-proposed.yaml` file over time.

## Generate the specification

### Setup

To initialize a local virtual environment, type the following commands in the root directory:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The virtual environment can be replaced with another local setup.

### Generate the API

Swagger has recently been added to the Trace Compass trace-server (reference implementation).

* Below is how to generate the TSP version, according to Swagger in trace-server.
* The generated TSP should match the current supported version of the TSP. Any differences may be pushed for review.
* `API.yaml` shows now the current supported version of the TSP.

1. Import all [TC][tracecompass] and [incubator][incubator] projects in Eclipse; branch, Target Platform and API Baseline set to `master`.
1. Open `traceserver.product` file in plug-in `org.eclipse.tracecompass.incubator.trace.server.product`.
1. Click on the `Run` button on the top right corner of the opened `traceserver.product`.
1. Browse [to here][apiyaml] ([swagger][swagger]) or so to generate server's TSP.
1. The resulting file is stored in the user's Downloads directory; e.g.: `~/Downloads/openapi.yaml`
1. Copy `~/Downloads/openapi.yaml` to this directory.
1. Update the latter with its license information and remove extra information: `./openapi.py`
1. The resulting diff between `API.yaml` and `openapi.yaml` can then be pushed for review.
   * Note, that the order of fields, components etc. might be different everytime the API is generated using swagger-core. This is due to how swagger-core is implemented.
1. Make sure to transfer the diffs to `API-proposed.yaml` as well.
1. `openapi.yaml` should not be merged to the repository and can be deleted when not needed anymore.

[apiProposed]: https://eclipse-cdt-cloud.github.io/trace-server-protocol/proposed/
[apiyaml]: http://localhost:8080/tsp/api/openapi.yaml
[incubator]: https://projects.eclipse.org/projects/tools.tracecompass.incubator/developer
[swagger]: https://github.com/swagger-api/swagger-core/wiki/Swagger-2.X---Integration-and-configuration#openapiresource
[tcServer]: https://download.eclipse.org/tracecompass.incubator/trace-server/rcp/
[tracecompass]: https://projects.eclipse.org/projects/tools.tracecompass/developer
[tspClient]: https://github.com/theia-ide/tsp-typescript-client
[tspGhPages]: https://theia-ide.github.io/trace-server-protocol/
[vscodeOpenapi]: https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi
