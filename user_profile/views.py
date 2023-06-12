from pyexpat.errors import messages
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserForm, EmailAuthenticationForm
from .models import MyUser


from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import MyUserForm

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



def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(data=request.POST)
        # login(request, form.get_user())
        return redirect('home')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'user_profile/login.html', {'form': form})



@login_required
def home_view(request):
    return render(request, 'user_profile/home.html')


# def logout_view(request):
#     logout(request)
#     return render(request, 'user_profile/login.html')

