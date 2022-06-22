from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fundraiser(models.Model):

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   Cause_name = models.CharField(max_length=50)
   tel = models.IntegerField()
   email = models.EmailField(max_length=254)
   Fundraiser_Type = models.CharField(max_length=50)
   Fundraiser_Duration = models.CharField(max_length=50)
   Target_Amount = models.IntegerField()

   def __str__(self):
      return self.name

