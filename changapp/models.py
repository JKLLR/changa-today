from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Fundraiser(models.Model):

   name = models.CharField(max_length=50)
   tel = models.IntegerField()
   email = models.EmailField(max_length=254)
   admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='fundraise')
   Fundraiser_Type = models.CharField(max_length=50)
   Fundraiser_Duration = models.CharField(max_length=50)
   Target_Amount = models.IntegerField()
    
   def __str__(self):
        return f'{self.name} fundraise'

   def create_fundraiser(self):
        self.save()

   def delete_fundraiser(self):
        self.delete()

   @classmethod
   def find_fundraiser(cls, fundraiser_id):
        return cls.objects.filter(id=fundraiser_id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=80, blank=True)
    bio = models.TextField(max_length=254, blank=True)
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()