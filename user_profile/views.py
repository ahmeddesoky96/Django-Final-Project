from django.shortcuts import render
from project.models import *
from .models import *
# Create your views here.

def listProject(request):
    p=Projects.objects.all()
    d=Donation.objects.all()
    c=Comment.objects.all()
    context={'p':p,'d':d,'c':c}
    return render(request,'user_profile/list_user_project.html',context)


