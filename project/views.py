from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *

# Create your views here.



### create project ###
#add
def createProject(req):
    # if('username' in req.session):
        context={}
        if(req.method=='POST'):
            myCategory = Category.objects.get(name='help')
            myEmail = MyUser.objects.get(id=1)
            Projects.objects.create(title=req.POST['title'],details=req.POST['details'],category=myCategory,target=req.POST['target'],start_date=req.POST['start_date'],end_date=req.POST['end_date'],owner_id=myEmail,report_count=1)
            return HttpResponseRedirect('/project/create')
        return render(req,'createProject.html',context)
       #id,title,details,category,target,start_date,end_date,owener_email,total_rate,repor_count

        

