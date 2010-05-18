function(doc) {
    if(doc.doc_type == "http://dropit.notmyidea.org/note"){
        summary = doc.content.substring(0, 140);
        emit(doc._id, {
            'title': doc.title, 
            'tags': doc.tags, 
            'summary': summary
        });
    }
}

