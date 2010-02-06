from django.conf.urls.defaults import *
from django.conf import settings

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'notes.views.list_notes', {}, 'home'),
    (r'^notes/', include('notes.urls', namespace='notes')),
    # (r'^admin/', include(admin.site.urls)),
    
)

# To serve static files. Do not use in production.
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DOC_ROOT}),
    )
