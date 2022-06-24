from django.contrib import admin
from .models import Profile, Fundraiser, Donate

# Register your models here.
admin.site.register(Profile)
admin.site.register(Fundraiser)
admin.site.register(Donate)