from couchdbkit.ext.django.schema import *

class Note(Document):
    """Represent a Note"""
    title = StringProperty(required=True)
    content = StringProperty(required=True)
    tags = StringListProperty()
    def __unicode__():
        return self.title+":\n"+content
