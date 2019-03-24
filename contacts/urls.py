from django.urls import path
from contacts import views

# app_name = 'listings'

urlpatterns = [
    path('contact', views.contact, name='contact'),
]
