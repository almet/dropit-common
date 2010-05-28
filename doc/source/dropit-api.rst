The CouchDB API
===============

Dropit is powered by a CouchDB documented database. The application is thinked
to be RESTful, and to work in a distributed way.

CouchDB comes with two important concept you should know about: views_ and
documents_. Please have a look at them before going further.

Keep in mind that with CouchDB infrastructure, you're free to add informations 
to the documents in your own couchdb db copy, but because we need a common base 
to work on, here are the 'specification' of our documents.

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

Please, refer to `the Note's specification document <note.html>`_ to get more 
informations about notes.

Associated views
----------------

To work with these notes, Dropit! provides a set of views_ you can find in the
`_design` folder on the dropit-common repository.

heads:
    Return all heading notes. So, 1 note per group of note/revision
by_root:
    Return all notes, with a key about their root.
history:
    List the history of all revisions, with [doc.root_note and doc.rev_number] 
    as key.
conflicts:
    Return the documents that are in a conflict state. This is useful for
    replication process. The client have to implement a method to handle the
    conflicts on the db and to resolve them. See the conflict.rst doc to know
    more.
tags:
    Return all the existing tags within the db.
by_tag:
    Return all the notes tagged with specific tags.
    Reduce by default.
summary:
    Return a simple summary of all existing notes (heads only).

.. _views: http://books.couchdb.org/relax/design-documents/views
.. _documents: http://books.couchdb.org/relax/intro/core-api#Documents
