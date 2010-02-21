from django.conf.urls.defaults import *

urlpatterns = patterns('notes.views',
    (r'^$', 'list_notes', {}, 'list'),
    (r'^new/$', 'add_note', {}, 'add'),
    (r'show/(?P<note_id>[a-z0-9]+)/$', 'show_note', {}, 'show'),
    (r'show/(?P<note_id>[a-z0-9]+)/(?P<rev>[a-z0-9]+)$', 'show_note', {}, 'show'),
    (r'delete/(?P<note_id>[a-z0-9]+)/$', 'delete_note', {}, 'delete'),
    (r'edit/(?P<note_id>[a-z0-9]+)/$', 'edit_note', {}, 'edit'),
    
)
