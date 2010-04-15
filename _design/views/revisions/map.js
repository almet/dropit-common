function(doc) {
    if (doc.doc_type == "http://dropit.notmyidea.org/note"){
       emit([note_id, doc._id], null);
    }
}
// myview startwith=['toto']&endwith=['toto', {}]
// return the list of revisions for the document named toto.
