from django.db import models
from datetime import datetime
# Create your models here.


class User(models.Model):
    firstname = models.CharField(max_length= 200)
    lastname = models.CharField(max_length=200 )
    email = models.EmailField(max_length=200, unique=True)
    text = models.TextField(blank=False)
    date = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.firstname







