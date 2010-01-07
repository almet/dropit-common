from django.shortcuts import render_to_response as render
from django.template import RequestContext, loader, Context
from notes.forms import NoteForm
from notes.models import Note

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
    note = Note.view.get(id=note_id)
    
    return render("show_note.html", {
        "note": note,
    })
    
def remove_note(request, note_id):
    """Delete a note and redirect to the list of notes
    
    """
    pass
