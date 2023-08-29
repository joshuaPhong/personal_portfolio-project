from django.shortcuts import render

#  IMPORT THE MODEL FOR THE PROJECT
from .models import Project


# Create your views here.
def home(request):
    # all the project objects/from database in the variable. an instance of
    # the Project model / class
    project_objects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'projectObjects': project_objects})
