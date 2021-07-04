from django.urls import path
from . import views

urlpatterns = [
    path ('', views.say_hi, name='home' ),
    path ('about', views.about, name='about'),
    path ('contacts', views.contact_info, name='contacts'),
    path ('django_boy', views.django_master, name='django_boy')
]
