from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('fundraiser/',views.start_fundraiser,name='fundraiser'),
    path('allfundraiser/',views.all_fundraisers,name='all_fundraiser'),

]