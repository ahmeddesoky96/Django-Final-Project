from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *

# Create your views here.
def myHome(req):
    top_rated_projects = top_rated_project(req)
    context={}
    context['top_rated_projects'] = top_rated_projects
    return render(req,'home.html',context)

def getCategory(req,str):
    return render(req,'category.html')


def top_rated_project(req):
    top_rated_projects = Projects.objects.order_by('-total_rate')[:5]
    return  top_rated_projects
