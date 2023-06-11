from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from project.models import *
from user_profile.models import *

# Create your views here.


def myHome(req):
    return render(req, 'home.html')


def getCategory(req, str):
    return render(req, 'category.html')


def image_slider(request):
    context = {}
    images = Image.objects.all()
    context['images'] = images
    return images
