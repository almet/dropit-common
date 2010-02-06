from django.conf.urls.defaults import *

urlpatterns = patterns('notes.views',
    (r'^$', 'list_notes', {}, 'list'),
    (r'^new/$', 'add_note', {}, 'add'),
    (r'show/(?P<note_id>[a-z0-9]+)/$', 'show_note', {}, 'show'),
    (r'remove/(?P<note_id>[a-z0-9]+)/$', 'remove_note', {}, 'remove'),
    (r'edit/(?P<note_id>[a-z0-9]+)/$', 'edit_note', {}, 'edit'),
    
)
