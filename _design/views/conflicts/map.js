function(doc) {
    if(doc._conflicts 
        && doc.doc_type == 'http://dropit.notmyidea.org/note') {
        emit(doc._conflicts, null);
    }
}
