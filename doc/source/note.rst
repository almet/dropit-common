Note specifications
===================

A note is defined by the following fields: 

Keep in mind that revisions are just older versions of a note. 

So, when we want to just get the list of documents (without all the 
history of each revision, we just have to check on the `is_revision` attribute 
of each note.

    * `_id` : the id of the note
    * `_rev` : the revision number (internal to CouchDB)
    * `title`: the title of the note
    * `tags` : differents tags about this note
    * `content`: the content text of the note
    * `date`: the date of the current note
    * `doc_type`: 'http://dropit.notmyidea.org/note'
    * `is_head` : true/false
    * `rev_number` : the revision number
    * `root_note` : the root's `_id`, if the document

Ideally, it's possible to add many other fields to a note. The first example 
that comes to my mind is a file.

_id and update workflow (for revisions)
---------------------------------------

By default, couchdb generate unique ids for each document, in dropit, we control
how the ids are generated, to handle conflicts between revisions.

For exemple, here is a scenario of id generation:

    # We create a note that does not exists, so we dont let couchdb generating 
      it's `id`. The first time you create a Note, the convention is to slugify 
      it's title. Ex: "my name is super monkey !" will produce the
      "my-name-is-super-monkey--" id.

    # We update the document, so we creates a new revision for this doc. We 
      *have* to generate manually (programatically) the id of the revision 
      document. The rule is to prefix the id of the parent document by the 
      number of the new revision. For the first revision, this will be 
      "2-my-name-is-supermonkey--", according to our exemple.

This conducts to a simple way for managing conflicts between revisions. 
For instance, let's imagine we have to persons who have the same document id 
on different couchdb databases, the document with the id `A`.

If both persons edit the same document on different databases, we will have one 
the couchdb1 and couchdb2, a document with the id `A`. When replicating the 
document on both databases, this will create a conflict, and we know how to 
resolve these conflicts.

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

