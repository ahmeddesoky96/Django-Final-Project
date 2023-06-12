from django.contrib import admin

from django.urls import path,include
from project.views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #for project urls
    path("project/",include('project.urls')),
    #for home urls
    path("home/",include('home.urls')),
    path("",include('user_profile.urls')),

    
]