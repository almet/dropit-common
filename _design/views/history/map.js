/**
 * List history of all revisions.
 *
 */
function(doc) {
    if (doc.doc_type == "http://dropit.notmyidea.org/note"){
            if (doc.root_note)
                emit([doc.root_note, doc.rev_number], doc);
            else
                emit([doc._id, doc.rev_number], doc);
    }
}

