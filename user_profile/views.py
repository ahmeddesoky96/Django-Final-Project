from django.shortcuts import render
from project.models import *
from .models import *
from django.db.models import Sum
# Create your views here.

def listProject(request):
    project_id=Projects.objects.filter(owner_id=2)
    sumlist = {}
    for j in project_id :
        total=Donation.objects.filter(project=j.id)
        sum= 0
        for i in total:
            sum+=i.donate_amount
        sumlist[j.id]=sum

    donation_id=Donation.objects.filter(user_id=1)
    context={'project_id':project_id,'donation_id':donation_id,'sumlist':sumlist}
    print(sumlist)
    return render(request,'user_profile/list_user_project.html',context)


