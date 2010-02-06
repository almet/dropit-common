from couchdbkit.ext.django.schema import *

class Note(Document):
    """Represents a Note document
    
    """
    title = StringProperty(required=True)
    content = StringProperty(required=True)
    tags = ListProperty()
    format = StringProperty()

    def __unicode__():
        return self.title+":\n"+self.content
