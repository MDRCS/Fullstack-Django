from django.urls import path
from .views import image_create

urlpatterns = [
    path('create/', image_create, name='create'),
]
