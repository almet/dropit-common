function(doc) {
	if(doc.itemType == "note")
		emit(doc.title,doc)
}
