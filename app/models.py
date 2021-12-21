from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    company_name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip   = models.IntegerField()
    email = models.EmailField()
    web = models.URLField()
    
    def __str__(self):
        return self.first_name+self.last_name
    
    