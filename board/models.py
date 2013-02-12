from django.db import models

# Create your models here.

class Categories( models.Model ):
    title = models.CharField(max_length = 40, null = False)

class WritingEntries( models.Model ):
    title = models.CharField(max_length = 80, null = False)
    content = models.TextField( null = False )
    createdDate = models.DateTimeField(auto_now_add = True, auto_now = True)
    category = models.ForeignKey(Categories)
    comments = models.PositiveSmallIntegerField( default = 0, null = True )

class CommentsModel( models.Model ):
    name = models.CharField(max_length = 20, null = False)
    password = models.CharField(max_length = 32, null = False)
    content = models.TextField(max_length = 2000, null = False)
    createdDate = models.DateTimeField(auto_now_add = True, auto_now = True)
    writingEntry = models.ForeignKey( WritingEntries )
