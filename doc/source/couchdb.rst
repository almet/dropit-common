The CouchDB API
===============

Dropit is powered by a CouchDB documented database. The application is thinked
to be RESTful, and to work in a distributed system. 

CouchDB comes with two important concept you should know about: views_ and 
documents_. Please have a look at them before going further.

Keep in mind that with CouchDB infrastructure, you're free to add informations 
to the documents in your own couchdb db copy, but because we need a common base 
to work on, here are the "specification" of our documents.

There's different kinds of documents, to distinguish between document types, 
we uses a `doc_type` field in all documents. Here are the full description of 
them:

Notes
-----

A note is basically a text, related to a set a subjects, named "tags". It has an
author and a title.

Fields
``````
* `Title`: the title of the note
* `Tags` : differents tags about this note
* `Content`: the content text of the note
* `Author`: the author name

Ideally, it's possible to add many other fields to a note. The first example 
that comes to my mind is a file.

Associated views
````````````````
To work with these notes, Dropit! provides a set of views_:

Tags
----


Users
-----

There's no users information stored directly in the couch, but our couch refers
to some users. Strange isn't it ? Don't be so sure, there is an explaination:

Because on how CouchDB is made, users aren't stored within the couch, but are 
stored in an external DB.


.. _views: http://books.couchdb.org/relax/design-documents/views
.. _documents: http://books.couchdb.org/relax/intro/core-api#Documents
