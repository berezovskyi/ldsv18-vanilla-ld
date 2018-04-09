# Vanilla Linked Data app

Adheres to the following [Linked Data principles](https://www.w3.org/DesignIssues/LinkedData.html):

1. Use URIs as names for things
2. Use HTTP URIs so that people can look up those names.
3. When someone looks up a URI, provide useful information, using the standards (RDF*, SPARQL)
4. Include links to other URIs. so that they can discover more things.

The last principle is only partly satisfied (no discovery).

3 [idempotent HTTP methods](https://stackoverflow.com/questions/45016234/what-is-idempotency-in-http-methods) are allowed: GET (for R in CRUD), PUT (for C & U in CRUD), DELETE (for D in CRUD).