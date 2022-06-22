from django import forms
from django.contrib.auth.models import User
from .models import Fundraiser

class FundraiserForm(forms.ModelForm):
   CATEGORIES = (
      ('', 'Select your fundraiser/Cause type'),
      ('Health','Health'),
      ('Education','Education'),
      ('Religious','Religious'),
      ('Wedding','Wedding'),
      ('Civil Society','Civil Society'),
      ('Business','Business'),
      ('Funeral', 'Funeral')
   )

   DURATIONS = (
      ('', 'Set fundraiser duration'),
      ('15 Days','15 Days'),
      ('30 Days','30 Days'),
      ('45 Days','45 Days'),
      ('60 Days','60 Days'),
      ('90 Days','90 Days')
   )
   Fundraiser_Type = forms.ChoiceField(choices=CATEGORIES,widget=forms.Select())
   Fundraiser_Duration = forms.ChoiceField(choices=DURATIONS,widget=forms.Select())
   class Meta:
      model = Fundraiser
      fields = ['name','tel','email','photo','Fundraiser_Type','Fundraiser_Duration','Target_Amount']