from django.urls import path
from .views import *


urlpatterns = [
    
    path('', myHome,name='myHome'),
    path('category', getCategory,name='myHome'),
    
]