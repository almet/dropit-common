/**
 * List tags
 */
function(doc) {
    if (doc.doc_type == "http://dropit.notmyidea.org/note"
        && doc.is_head == true
        && doc.tags.length > 0){
        for(var tag in doc.tags) {
            emit(doc.tags[tag], doc);
        }
    }
}
