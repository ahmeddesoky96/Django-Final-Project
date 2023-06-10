from django.urls import path
from .views import *


urlpatterns = [
    
    path('', listProject,name='listproject'),
    
]