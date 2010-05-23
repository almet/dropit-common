/**
 * List history of all revisions.
 *
 */
function(doc) {
    if (doc.doc_type == "http://dropit.notmyidea.org/note"){
            if (doc.root_note)
                emit([doc.root_note, doc._id], doc);
            else
                emit([doc._id, doc._id], doc);
    }
}

