from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from project.models import *
from django.db.models import Sum



# Create your views here.
def UserInfo(request):
    if('username' in request.session):
        user_projects = get_projects_with_donations(request.session['user_id'])
        all_donations = get_all_donations(request.session['user_id'])
        context = {}
        user_data= MyUser.objects.get(id=request.session['user_id'])
        context['user_projects'] = user_projects
        context['all_donations'] = all_donations
        # print(user_data.birth_date)
        context['user']=user_data
        return render(request, 'User/User_info.html', context)
    else:
        return redirect("/Registeration")
    

def EditUserInfo(req):
    if('username' in req.session):
        context = {}
        user = MyUser.objects.get(id=req.session['user_id'])  # Retrieve the user instance with ID 1
        context['user'] = user
        if req.method == "POST":
            # Update the fields of the retrieved instance
            user.first_name = req.POST['first_name']
            user.last_name = req.POST['last_name']
            # user.birth_date = req.POST['birth_date']
            user.email = req.POST['email']
            user.image = req.FILES['image']
            user.password = req.POST['password']
            user.phone_number = req.POST['phone_number']
            user.facebook_profile = req.POST['facebook_profile']
            user.country = req.POST['country']
            user.save()  # Save the updates to the database
            return HttpResponseRedirect('/user')
        return render(req, 'User/User_edit.html', context)
    else:
        return redirect("/Registeration")

def EditUser(req):
    return HttpResponseRedirect('/user/edit')

def get_projects_with_donations(owner_id):
    projects = Projects.objects.filter(owner_id=owner_id)
    result = []
    for project in projects:
        total_donations = Donation.objects.filter(project=project.id).aggregate(Sum('donate_amount'))['donate_amount__sum'] or 0
        project_dict = {
            'id': project.id,
            'title': project.title,
            'details': project.details,
            'category': project.category,
            'owner_id': project.owner_id,
            'target': project.target,
            'total_rate': project.total_rate,
            'total_donations': total_donations,
        }
        result.append(project_dict)
    return result

def get_all_donations(id):
    donations= Donation.objects.filter(user_id=id)
    all_project = []
    for donate in donations:
        project = Projects.objects.get(id=donate.id)
        project_dict = {
            'id': project.id,
            'project': project.title,
            'amount': donate.donate_amount,        
        }
        all_project.append(project_dict)
    return all_project
    
    