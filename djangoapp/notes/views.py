from django.shortcuts import render_to_response as render 
from django.template import RequestContext, loader, Context 
from django.utils.encoding import smart_str, force_unicode

from couchdbkit.ext.django.loading import get_db

from notes.forms import NoteForm 
from notes.models import Note
from utils.shortcuts import get_object_or_404

def add_note(request):
    """Add a note
        - GET request display the form
        - POST request create the note and redirect if the add is successful
    """
    note = None

    if request.POST:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
    else:
        form = NoteForm()

    return render("add_note.html", {
        "form": form,
        "note": note,
    })


def list_notes(request):
    """List all notes

    """
    notes = Note.view('notes/all')
    return render("list_notes.html", {
        "notes": notes,
    })


def show_note(request, note_id):
    """Display a note in detail

    """
    note = get_object_or_404(Note, note_id)
    
    if note.format == "rst":
        from docutils.core import publish_parts
        parts = publish_parts(source=smart_str(note.content), writer_name="html4css1")
        note.content = force_unicode(parts["html_body"])
        
    revisions = get_db("notes").doc_revisions(note_id)['_revisions']
    
    return render("show_note.html", {
        "note": note,
        "has_revisions" : revisions['start'] > 1,
        "revisions": revisions['ids'],
    })

def edit_note(request, note_id):
    pass

def remove_note(request, note_id):
    """Delete a note and redirect to the list of notes

    """
    pass
