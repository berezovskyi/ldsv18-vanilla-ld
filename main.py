#!/usr/bin/env python

'''
Copyright (c) 2018 Andrew Berezovskyi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from rdflib import Graph, BNode, Literal, URIRef
from rdflib.namespace import FOAF
from flask import Flask, abort, g, request
import flask_rdf
from flask_rdf.flask import returns_rdf
from flask_rdf.format import formats
import random

app = Flask(__name__)

graphs = {}

'''
Well, there is no standard way in vanilla RDF/HTTP pair to discover operations.
There is 'OPTIONS *' (as opposed to 'OPTIONS /') but we need to send RDF over
it that describes the API. See:
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS
  - https://www.w3.org/Submission/OWL-S/
  - https://www.w3.org/Submission/WSMO/
  - https://www.w3.org/Submission/SWSF-SWSO/
'''
@app.route('/', methods=['GET'])
def get_home():
  abort(404)

'''
No need for this method, just to be explicit
'''
@app.route('/', methods=['PUT', 'POST', 'DELETE'])
def put_home():
  abort(405)


@app.route('/<path:path>', methods=['GET'])
@returns_rdf
def get_resource(path=''):
  if path in graphs:
    return graphs[path]
  else:
    abort(404)

@app.route('/<path:path>', methods=['PUT'])
def put_resource(path=''):
    graph = Graph('IOMemory', BNode())
    graph.parse(data=request.data, format=formats[request.mimetype])
    new = False if path in graphs else True
    graphs[path] = graph
    code = 201 if new else 200
    return '', code

@app.route('/<path:path>', methods=['DELETE'])
def delete_resource(path=''):
  code = 204 # No Content
  if path in graphs:
    del graphs[path]
  else:
    code = 400 # Bad Request
  return '', code

if __name__ == '__main__':
  flask_rdf.add_format('application/ld+json', 'json-ld')
  app.run(host='127.0.0.1', debug=True)