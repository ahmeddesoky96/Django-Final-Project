from django.urls import path
from .views import project_search

urlpatterns = [
    path('search/', project_search, name='project_search'),
]
