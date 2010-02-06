from django.http import Http404

def get_object_or_404(klass, *args, **kwargs):
    try:
        if args:
            return klass.get(*args)
        elif kwargs:
            return klass.get(**kwargs)
    except:
         raise Http404('No record matches the given query.')
