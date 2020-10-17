from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    phone_number = models.CharField(max_length = 10)
    status = models.BooleanField()


        