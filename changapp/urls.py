from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name = 'home'),
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('about/', views.about, name='about'),
    path('fundraiser/',views.start_fundraiser,name='fundraiser'),
    path('allfundraiser/',views.all_fundraisers,name='all_fundraiser'),
    path('success/', views.success, name="success"),
    path('<fundraise_id>/donate', views.donate, name='donate'),
    path('paypal/', views.paypal, name='paypal'),
    path('signout/',views.signout,name='signout'),
]