from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

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
        return self.user.username

#    @receiver(post_save, sender=User)
#    def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Fundraiser.objects.create(user=instance)

#    @receiver(post_save, sender=User)
#    def save_user_fundraiser(sender, instance, **kwargs):
#         instance.profile.save()

