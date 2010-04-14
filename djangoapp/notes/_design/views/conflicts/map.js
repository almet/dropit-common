function(doc) {
  if(doc._conflicts && doc.itemType == 'revisions') {
    emit(doc._conflicts, null);
  }
}
