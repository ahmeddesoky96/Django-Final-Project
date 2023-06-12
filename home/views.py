from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *

# Create your views here.
def myHome(req):
    context={}
    myCategory=allCategory(req)
    context['allCategory']=myCategory
    return render(req,'home.html',context)

def getCategory(req,cate):
        context={}
        req.session['categoryN']=cate
        context['category']=Category.objects.filter(name=cate)
        context['projects']=Projects.objects.filter(category=cate)
        
        return render(req,'category.html',context)

def allCategory(req):
      context={}
      all_category=Category.objects.all()
      return all_category
    