from django.shortcuts import render
from project.models import *
from .models import *
from django.db.models import Sum
# Create your views here.

def get_projects_with_donations(request):
    owner_id = request.GET.get('id')
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
    context = {'result': result}
    return render(request, 'user_profile/list_user_project.html', context)

