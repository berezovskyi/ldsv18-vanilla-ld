# Vanilla Linked Data app

## Intro

Adheres to the following [Linked Data principles](https://www.w3.org/DesignIssues/LinkedData.html):

1. Use URIs as names for things
2. Use HTTP URIs so that people can look up those names.
3. When someone looks up a URI, provide useful information, using the standards (RDF*, SPARQL)
4. Include links to other URIs. so that they can discover more things.

The last principle is only partly satisfied (no discovery).

3 [idempotent HTTP methods](https://stackoverflow.com/questions/45016234/what-is-idempotency-in-http-methods) are allowed: GET (for R in CRUD), PUT (for C & U in CRUD), DELETE (for D in CRUD).

## Getting started

Run using Python:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```

Use curl to make some HTTP requests:

```sh
$ curl -s -i -X PUT http://127.0.0.1:5000/test -H 'Content-Type: application/ld+json' --data-binary '{"@context":{"name":"http://xmlns.com/foaf/0.1/name"}, "name":"Alice"}'
HTTP/1.1 201 CREATED
...

$ curl -s -i http://127.0.0.1:5000/test -H 'Accept: application/ld+json' 
HTTP/1.1 200 OK
Server: Werkzeug/3.1.4 Python/3.12.1
Date: Tue, 23 Dec 2025 11:51:47 GMT
Content-Type: application/ld+json
Content-Length: 149
Vary: Accept
Connection: close

[
  {
    "@id": "_:N56db991fbee64c4c9160ef24d7b5e6e1",
    "http://xmlns.com/foaf/0.1/name": [
      {
        "@value": "Alice"
      }
    ]
  }
]
```