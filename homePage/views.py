from django.shortcuts import render
from project.models import Tag
from project.models import Project


def project_search(request):
    if request.method == 'GET':
        form = ProjectSearchForm(request.GET)
        if form.is_valid():
            tag_name = form.cleaned_data['tag_name']
            projects = Project.objects.filter(tags__name__icontains=tag_name)
        else:
            projects = Project.objects.all()
    else:
        form = ProjectSearchForm()
        projects = Project.objects.all()

    context = {
        'form': form,
        'projects': projects
    }
    return render(request, 'project_search.html', context)
