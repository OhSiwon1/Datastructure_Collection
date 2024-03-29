from django.shortcuts import render
from .models import Project, Comment


# Create your views here.
def main(request):
    #project_list = Project.objects.order_by('-harts')
    
    return render(request, 'DS/main.html')

