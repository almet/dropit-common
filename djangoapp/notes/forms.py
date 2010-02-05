from couchdbkit.ext.django.forms import *
from django import forms
from notes.models import Note

class NoteForm(DocumentForm):
    "form to edit a note"
    title = forms.CharField()
    content = forms.CharField()
    tags =  forms.CharField()
    class Meta:
        document = Note
