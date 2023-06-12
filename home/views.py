from django.shortcuts import render , redirect
from django.http import HttpResponse ,HttpResponseRedirect
from project.models import *
from user_profile.models import *
from django.db.models import Sum
from django.db.models import Q
# #########################################################
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MyUserForm, EmailAuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# # Create your views here.
# def myHome(req):
    
#     top_rated_projects = top_rated_project(req)
#     latest_projects = latest_project(req)
    
#     myCategory=allCategory(req)
#     admin_projects_selected = admin_projects(req)
    
#     if req.method=='POST':
#         search_result = searchBar(req)
#         context = {}
#         context['search_result'] = search_result
#         return render(req,'home/search.html',context)
    
#     context={}
#     context['allCategory']=myCategory
#     context['top_rated_projects'] = top_rated_projects
#     context['latest_projects'] = latest_projects
#     context['admin_projects_selected'] = admin_projects_selected

#     return render(req,'home.html',context)

# #################################################################################################

def myHome(req):
    if req.user.is_authenticated:
        top_rated_projects = top_rated_project(req)
        latest_projects = latest_project(req)

        myCategory = allCategory(req)
        admin_projects_selected = admin_projects(req)

        if req.method == 'POST':
            search_result = searchBar(req)
            context = {}
            context['search_result'] = search_result
            return render(req, 'home/search.html', context)

        context = {}
        context['allCategory'] = myCategory
        context['top_rated_projects'] = top_rated_projects
        context['latest_projects'] = latest_projects
        context['admin_projects_selected'] = admin_projects_selected

        return render(req, 'home.html', context)
    else:
        return redirect('login')


# ############################################################################################

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


# ################################################################################################################


def create_user(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            # Extract form data
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            # Check if confirm_password is equal to password
            if password != confirm_password:
                form.add_error('confirm_password', 'The passwords do not match.')
                return render(request, 'user_profile/create_user.html', {'form': form})

            # Create new user with custom username
            username = first_name.lower().replace(' ', '')
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.is_active = False
            user.save()

            return redirect('login')
    else:
        form = MyUserForm()
    return render(request, 'user_profile/create_user.html', {'form': form})



# def login_view(request):
#     if request.method == 'POST':
#         form = EmailAuthenticationForm(data=request.POST)
#         # login(request, form.get_user())
#         # return redirect('home')
#         return render(request, 'home.html')
#     else:
#         form = EmailAuthenticationForm()
#     return render(request, 'user_profile/login.html', {'form': form})

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        # If authentication fails, render the login form with an error message
        error_message = 'Invalid email or password.'
    else:
        error_message = None
    form = EmailAuthenticationForm()
    return render(request, 'user_profile/login.html', {'form': form, 'error_message': error_message})



@login_required
def home_view(request):
    return render(request, 'user_profile/home.html')


# def logout_view(request):
#     logout(request)
#     return render(request, 'user_profile/login.html')

