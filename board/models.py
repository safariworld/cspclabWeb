from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

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
    attachedFile = models.FileField(upload_to='attachments', null = True, blank=True) #attach file.
    user = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.title

class CommentsModel( models.Model ):
    content = models.TextField(max_length = 2000, null = False)
    createdDate = models.DateTimeField(auto_now = True)
    writingEntry = models.ForeignKey( WritingEntries )
    user = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.content
