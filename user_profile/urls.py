from django.urls import path
from .views import *


urlpatterns = [
    
    path('', get_projects_with_donations,name='listproject'),
    
]