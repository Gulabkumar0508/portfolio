from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    message = models.TextField(null=True,blank=True)