function(doc) {
	if(doc.doc_type == "Note")
		emit(doc.title,doc)
}
