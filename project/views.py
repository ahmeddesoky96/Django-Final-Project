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
            Projects.objects.create(title=req.POST['title'],details=req.POST['details'],category=myCategory,target=req.POST['target'],start_date=req.POST['start_date'],end_date=req.POST['end_date'],owner_id=myEmail,repor_count=1)
            return HttpResponseRedirect('/project/create')
        return render(req,'createProject.html',context)
       #id,title,details,category,target,start_date,end_date,owener_email,total_rate,repor_count

        


def get_similar_project(req, id):
    # Get the tags of the project with the given ID.
    proj_tags = Tag.objects.filter(project=id).values_list('tag_name', flat=True)

    # Get other projects that have tags similar to the current project.
    sim_projs = Tag.objects.filter(tag_name__in=proj_tags).exclude(project=id).values_list('project', flat=True)

    # Get four random projects from the similar projects.
    random_proj = Projects.objects.filter(id__in=sim_projs).order_by('?')[:4]

    context = {}
    context['random_proj'] = random_proj
    return render(req, 'display_proj.html', context)