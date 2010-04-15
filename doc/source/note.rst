Note
====

A note is defined by the following fields: 

    * `_id` : the id of the note
    * `_rev` : the revision number (internal to CouchDB)
    * `title`: the title of the note
    * `tags` : differents tags about this note
    * `content`: the content text of the note
    * `content_format`: the input format of the text
    * `date`: the date of the current note
    * `doc_type`: 'http://dropit.notmyidea.org/note'
    * `is_revision` : true/false
    * `parent_note` : the parent's `_id`.

Ideally, it's possible to add many other fields to a note. The first example 
that comes to my mind is a file.

_id
----

By default, couchdb generate unique ids for each document, in dropit, we control
how the ids are generated, to handle conflicts.

The first time you create a Note, the convention is to slugify it's title.
Ex: "my name is super monkey !" will be replaced by "ma-name-is-super-monkey--".

tags
----

Tags are a list of texts. Exemple:
["tag1", "tag2", "tag3"]

content_format
--------------

The content format of the note (html, ...)

Caution ! The `content_format` is *only* a meta data information, to know how to
work with this content. How to 'decode' it. This does not affect how the content
is stored in couchdb. Notes are *always* stored in RAW text.

