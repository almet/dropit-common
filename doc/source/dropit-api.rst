The CouchDB API
===============

Dropit is powered by a CouchDB documented database. The application is thinked
to be RESTful, and to work in a distributed way.

CouchDB comes with two important concept you should know about: views_ and
documents_. Please have a look at them before going further.

Keep in mind that with CouchDB infrastructure, you're free to add informations
to the documents in your own couchdb db copy, but because we need a common base
to work on, here are the "specification" of our documents.

There's different kinds of documents, to distinguish between document types,
we uses a `doc_type` field in all documents. Here are the full description of
them:

Databases / Users
-----------------

Dropit consider having a table by user. As it's pretty simple to create new
databases, it seems to be a good idea.

Each database is named with the name of the user. for instance, the user
`alexis` will have a db named `alexis` too, that belongs to him.

Notes
-----

A note is basically a text, related to a set a subjects, named "tags". It has an
author and a title.

Fields
``````
Here is the list of fields for a simple note.

    * `title`: the title of the note
    * `tags` : differents tags about this note
    * `content`: the content text of the note
    * `input_format`: the input format of the text
    * `doc_type`: "Note"

Caution ! The `input_format` is *only* a meta data information, to know how to
work with this content. How to "decode" it. This does not affect how the content
is stored in couchdb. Notes are *always* stored in RAW text.

Ideally, it's possible to add many other fields to a note. The first example
that comes to my mind is a file.

Here is a list of all other known fields:

 * File

It's interesting to see the standard defined by desktopcouch here: http://www.freedesktop.org/wiki/Specifications/desktopcouch/note

Associated views
----------------

To work with these notes, Dropit! provides a set of views_ you can find in the
`_design` folder on the dropit-common repository.

all:
    Return all documents for an user (inside a DB)
by_rev:
    Return documents by revision number. Return all documents with the specified
    revision number
conflicts:
    Return the documents that are in a conflict state. This is useful for
    replication process. The client have to implement a method to handle the
    conflicts on the db and to resolve them.
tags:
    Return all the existing tags for the user
by_tag:
    Return all the note tagged with a specified tag

.. _views: http://books.couchdb.org/relax/design-documents/views
.. _documents: http://books.couchdb.org/relax/intro/core-api#Documents
