from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *
from django.db.models import Sum
from django.db.models import Q


# Create your views here.
def myHome(req):
    
    top_rated_projects = top_rated_project(req)
    latest_projects = latest_project(req)
    
    myCategory=allCategory(req)
    admin_projects_selected = admin_projects(req)
    
    if req.method=='POST':
        search_result = searchBar(req)
        context = {}
        context['search_result'] = search_result
        return render(req,'home/search.html',context)
    
    context={}
    context['allCategory']=myCategory
    context['top_rated_projects'] = top_rated_projects
    context['latest_projects'] = latest_projects
    context['admin_projects_selected'] = admin_projects_selected

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
    

def admin_projects(req):
    admin_selected = Adminproject.objects.all()[:5]
    proj_list = []
    for obj in admin_selected:
        proj = Projects.objects.get(id=obj.id)
        proj_list.append(proj)
    return proj_list


def top_rated_project(req):
    top_rated_projects = Projects.objects.order_by('-total_rate')[:5]
    return  top_rated_projects

def latest_project(req):
    latest_projects = Projects.objects.order_by('-created_at')[:5]
    return latest_projects


def check_donation_percentage(id):
    project = Projects.objects.get(id=id)
    total_donations = Donation.objects.filter(project=id).aggregate(Sum('donate_amount'))['donate_amount__sum'] or 0
    return True if total_donations < 0.25 * project.target else False



def get_projects_with_donations(owner_id):
    projects = Projects.objects.filter(owner_id=owner_id)
    result = []
    for project in projects:
        total_donations = Donation.objects.filter(project=project.id).aggregate(Sum('donate_amount'))['donate_amount__sum'] or 0
        project_dict = {
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'target': project.target,
            'total_donations': total_donations,
        }
        result.append(project_dict)
    return result



def searchBar(request):

    search_word = request.POST['search']
    tag_data = Tag.objects.filter(tag_name__icontains=search_word)
    project_data = Projects.objects.filter(Q(title__icontains=search_word) | Q(tag__in=tag_data)).distinct()
    return project_data


