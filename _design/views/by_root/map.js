/**
 * Return all notes, with a key about their root
 */
function(doc){
    if (doc.doc_type == "http://dropit.notmyidea.org/note"){
        if (doc.root_note){
            emit(doc.root_note, doc);
        }
        else{
            // it's the root note !
            emit(doc._id, doc);
        }
    }
}

    
