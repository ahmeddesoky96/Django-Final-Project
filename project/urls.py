from django.urls import path
from .views import *


urlpatterns = [
    
    path('create', createProject,name='createProject'),
    path('<int:id>', get_similar_project,name='get_similar_project'),
    
]