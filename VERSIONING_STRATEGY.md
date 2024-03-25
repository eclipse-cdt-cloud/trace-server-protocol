# TSP Versioning Strategy

At the moment, TSP is not yet at version 1.0.0.
As such, we are expecting breaking changes to occur quite often until we reach V1.

Once we do achieve such a milestone, a versioning and deprecation strategy will need to be implemented to maintain and update the TSP. This document will outline this strategy and why certain choices where made regarding the versioning of the TSP.

There are generally 3 main ways of versioning a REST API:

- [URL / URI Versioning](#url--uri-versioning)
- [Query Parameters Versioning](#query-parameters-versioning)
- [Custom Headers Versioning](#custom-headers-versioning)

## URL / URI Versioning

The URL could look something like this: `/tsp/api/v2/experiments/...`

Pros:

- Most visible for users.
- Easiest to understand and implement.
- Industry standard.

Cons:

- Can lead to URL pollution.
- In our current implementation of the TSP, it can lead to duplicated code to support multiple versions. As such, a deprecation startegy must be devised to avoid supporting multiple versions for too long.

Best use: versioning the whole API instead of versioning specific endpoints.

## Query Parameters Versioning

The URL could look something like this: `/tsp/api/v2/experiments?version=2/...`

Pros:

- Good user visibility.
- Easy to understand and implement.

Cons:

- Increased URL pollution.
- Can lead to caching issues.
- Can lead to version differences between specific endpoints, depending on the implementation. This can be confusing for the user of the API.

Best use: quick prototyping / testing or for versioning specific endpoints.

## Custom Headers Versioning

This technique involves sending a header with the request which might contain something like: `Accept: version=2.0`

Pros:

- URL is kept clean and uncluttered.
- Best practice for REST APIs, since the versioning is decoupled from the resources URIs.

Cons:

- Less visibility.
- Harder to understand for the end user. He has to send a header with the version number instead of changing the URL.
- Hard to determine if the version number refers to an endpoint or to the whole API.

Best use: complex scenarios.

## Decision Taken

Once the TSP is stable enough for Version 1.0.0, we will proceed with URL versioning as it is the industry standard and it offers the most visibility for users. In due time, a deprecation strategy will be formulated to avoid having to support multiple versions of the API, which can lead to duplicated code in the codebase.
