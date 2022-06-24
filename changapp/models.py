import email
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

class Fundraiser(models.Model):

   name = models.CharField(max_length=50)
   tel = models.IntegerField()
   email = models.EmailField(max_length=254)
   admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='fundraise')
   photo =CloudinaryField('images')
   description = models.TextField(blank=True)
   Fundraiser_Type = models.CharField(max_length=50)
   Fundraiser_Duration = models.CharField(max_length=50)
   Target_Amount = models.IntegerField()
   date = models.DateTimeField(auto_now_add=True, blank=True)
    
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


# class Rating(models.Model):
    
#     score = models.FloatField(default=0, blank=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='ratings', null=True)

#     def save_rating(self):
#         self.save()

#     @classmethod
#     def get_ratings(cls, id):
#         ratings = Rating.objects.filter(post_id=id).all()
#         return ratings

#     def __str__(self):
#         return f'{self.post} Rating'

# class Donate(models.Model):
    
#     email = models.EmailField(max_length=254)
#     donation_amount = models.IntegerField()
#     fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE,related_name='donations')
#     date = models.DateTimeField(auto_now_add =True,null=True)

#     def __str__(self):
#         return self.donation_amount


class Donate(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    donation_amount = models.IntegerField()
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE,related_name='fundraiser_donation')
    date = models.DateTimeField(auto_now_add =True,null=True)

    # def __str__(self):
    #     return f'{self.name} Business'

    # def create_donation(self):
    #     self.save()

    # def delete_donation(self):
    #     self.delete()

    # @classmethod
    # def search_donation(cls, name):
    #     return cls.objects.filter(name__icontains=name).all()