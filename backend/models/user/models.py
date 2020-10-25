from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    status = models.BooleanField()

    def __str__(self): 
        return self.name

#class Product(models.Model):
 #   id = models.AutoField( primary_key = True)
  #  name = models.CharField( max_length = 50)
   # provider = models.CharField( max_length = 50)
    #category = models.CharField( max_length = 50)
    #price = models.FloatField()