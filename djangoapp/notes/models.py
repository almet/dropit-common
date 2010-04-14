from couchdbkit.ext.django.schema import *

class Note(Document):
    """Represents a Note document
    
    """
    title = StringProperty(required=True)
    content = StringProperty(required=True)
    tags = ListProperty()
    format = StringProperty()
    itemType = StringProperty(default='note')

    def __unicode__():
        return self.title+":\n"+self.content
    
    def get_note(id, rev_id=None):
        """Retreive a note by it's id plus the rev_id if one is provided.
        
        """
        self.
