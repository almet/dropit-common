function(doc) {
	if(doc.itemType == "http://dropit.notmyidea.org/note"){
		emit(doc._id, doc);
    }
}
