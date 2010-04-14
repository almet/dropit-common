function(doc) {
	if (doc.itemType == "note")
		emit([doc.id, 0],doc)
	if (doc.itemType == "revision" && doc.parentNote)
	    // foreach revision, emit it
	    emit([doc.parent, 1], rev)
}
