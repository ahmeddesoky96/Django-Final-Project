from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect

#################  Edit User Info   #######################################################################################
def EditUserInfo(req):
    context = {}
    user = MyUser.objects.get(id=1)  # Retrieve the user instance with ID 1
    context['user'] = user
    if req.method == "POST":
        # Update the fields of the retrieved instance
        user.first_name = req.POST['first_name']
        user.last_name = req.POST['last_name']
        # user.birth_date = req.POST['birth_date']
        user.email = req.POST['email']
        user.image = req.FILES['image']
        user.phone_number = req.POST['phone_number']
        user.facebook_profile = req.POST['facebook_profile']
        user.country = req.POST['country']
        user.save()  # Save the updates to the database
        return HttpResponseRedirect('/user')
    return render(req, 'User/User_edit.html', context)


#################  Edit User Info   ########################################################################################################################################
def UserInfo(request):
    context = {}
    T= MyUser.objects.get(id=1)
    context['user']=T
    return render(request, 'User/User_info.html', context)
    # user = request.user

#######################################################################################################################################################



def EditUser(req):
    return HttpResponseRedirect('/user/edit')
