from django.db import models

# Create your models here.

class Categories( models.Model ):
    title = models.CharField(max_length = 40, null = False)
    
    def __unicode__(self):
        return self.title

class WritingEntries( models.Model ):
    title = models.CharField(max_length = 80, null = False)
    content = models.TextField( null = False )
    createdDate = models.DateTimeField(auto_now_add = True)
    updatedDate = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Categories)
    comments = models.PositiveSmallIntegerField( default = 0, null = True )
    attachedFile = models.FileField(upload_to='attachments', null = True) #attach file.
    
    def __unicode__(self):
        return self.title


class CommentsModel( models.Model ):
    name = models.CharField(max_length = 20, null = False)
    password = models.CharField(max_length = 32, null = False)
    content = models.TextField(max_length = 2000, null = False)
    createdDate = models.DateTimeField(auto_now = True)
    writingEntry = models.ForeignKey( WritingEntries )
    
    def __unicode__(self):
        return self.content
