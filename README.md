# trace-server-protocol

Specification of the Trace Server Protocol

This protocol is built to decouple the backend and frontend of trace analysers, allowing traces to reside and be analysed on the backend, and visual models to be exchanged with a variety of clients.

The protocol is meant to be RESTful, over HTTP.

The specification is currently written in **OpenAPI 3.0** and can be pretty-visualized in the [github pages][tspGhPages].

## HOW-TO

The specification should be edited with the [OpenAPI (Swagger) Editor extension][vscodeOpenapi] for VS Code.

The latter extension is assumed for consistent formatting of the `./API.yaml` file over time.

### Setup

To initialize a local virtual environment, type the following commands in the root directory:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The virtual environment can be replaced with another local setup.

### Alternate TSP version

Above, `API.yaml` has been the manually documented TSP version up until now.

* That version is the one shown by the default [github pages][tspGhPages].
* That version does not fully match what [Incubator][incubator]'s trace-server currently supports.
  * Some TSP endpoints differ or are missing in trace-server, despite its use to help refine the protocol.
  * That trace-server being the TSP reference implementation, among potential other ones.
* Aligning the TSP documented that way with trace-server's own (reference) endpoints is a work in progress.

In the meantime, Swagger has recently been added to trace-server.

* Below is how to generate the alternate TSP version, according to Swagger in trace-server.
* This alternate version is to be gradually augmented based on what has been manually documented through `API.yaml`.
* [Swagger github pages][tspSwagger] show this alternate version to grow.
* `API.yaml` should gradually become the wanted version of the TSP, as this alternate one shows the reference TSP.
* Such reference and future (forecasted) TSP versions will be documented accordingly as these yaml files evolve.

1. Import all [TC][tracecompass] and [incubator][incubator] projects in Eclipse; branch, Target Platform and API Baseline set to `master`.
1. Open `traceserver.product` file in plug-in `org.eclipse.tracecompass.incubator.trace.server.product`
1. Click on the `Run` button on the top right corner of the opened `traceserver.product`
1. Browse [to here][apiyaml] ([swagger][swagger]) or so to generate server's TSP.
1. Bring the resulting file over; e.g.: `mv ~/Downloads/openapi.yaml .`
1. Update the latter with its license information and remove extra information: `./openapi.py`
1. The resulting git diff may then be pushed for review, at will.

[1] org.eclipse.tracecompass.incubator.trace.server.jersey.rest.core

[tracecompass]: https://projects.eclipse.org/projects/tools.tracecompass/developer
[incubator]: https://projects.eclipse.org/projects/tools.tracecompass.incubator/developer
[apiyaml]: http://localhost:8080/tsp/api/openapi.yaml
[swagger]: https://github.com/swagger-api/swagger-core/wiki/Swagger-2.X---Integration-and-configuration#openapiresource
[tspGhPages]: https://theia-ide.github.io/trace-server-protocol/
[tspSwagger]: https://theia-ide.github.io/trace-server-protocol/swagger/
[vscodeOpenapi]: https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi
