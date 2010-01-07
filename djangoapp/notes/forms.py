from couchdbkit.ext.django.forms import *
from notes.models import Note

class NoteForm(DocumentForm):
    "form to edit a note"    
    class Meta:
        document = Note
