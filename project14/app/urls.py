from django.urls import path
from .views import *
urlpatterns = [
    path('django_register', django_register, name='django_register'),
    path('model_register', model_register, name='model_register')
]
