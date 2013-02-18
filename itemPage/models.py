from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class itemList( models.Model ):
    itemCode = models.CharField( max_length = 5, primary_key = True )
    itemName = models.CharField( max_length = 100, null = False )	
    available = models.BooleanField( default = True )
	
class borrowedList( models.Model ):
    itemCode = models.ForeignKey( itemList, related_name='code' )
    userId = models.ForeignKey( User )
    borrowedDate = models.DateTimeField( auto_now_add = True )
    returnDate = models.DateTimeField( auto_now = True, null = True )
