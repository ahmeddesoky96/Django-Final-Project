from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    
    path('', myHome,name='myHome'),
    path('category/<str:cate>', getCategory,name='category'),
    path('register/', create_user, name='create_user'),
    path('login/', login_view, name='login'),
    path('home/', login_required(home_view, login_url='login'), name='home'),
    path('logout/', login_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)