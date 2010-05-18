/**
 * List last versions of each documents
 * (called heads)
 */
function(doc) {
	if(doc.doc_type == "http://dropit.notmyidea.org/note" 
        && doc.is_head == true){
		emit(doc._id, doc);
    }
}
