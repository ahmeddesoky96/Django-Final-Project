from django.shortcuts import render
from project.models import *
from .models import *
from django.db.models import Sum
# Create your views here.

def listProject(request):
    p=Projects.objects.filter(owner_id=2)
    sumlist = {}
    for j in p :
        total=Donation.objects.filter(project=j.id)
        sum= 0
        for i in total:
            sum+=i.donate_amount
        sumlist[j.id]=sum

    d=Donation.objects.filter(user_id=1)
    context={'p':p,'d':d,'sumlist':sumlist}
    print(sumlist)
    return render(request,'user_profile/list_user_project.html',context)


