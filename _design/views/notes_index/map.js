function(doc) {
	if(doc.itemType == "http://dropit.notmyidea.org/note"){
        summary = 'kikoolol'; 
		emit(doc.id, [doc.title, doc.tag, doc.date, summary])
    }
}
