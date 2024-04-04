from django.shortcuts import render,redirect
from .models import Project, Comment, Year
from DS.forms import ProjectForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    year_list = Year.objects.order_by()
    context = {'year_list':year_list }        
    return render(request, 'DS/main.html', context)

def ProjectsByYears_view(request,year_id):
    year = Year.objects.get(id=year_id)
    context = {'year': year}
    return render(request,'DS/ProjectsByYears.html', context)


def detail_view(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'DS/project_detail.html', context)

@login_required(login_url='common:login')
def comments_create(request,project_id):
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.author = request.user 
            comment.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = CommentForm()
    context = {'project': project, 'form': form}
    return render(request, 'DS/project_detail.html', context)

@login_required(login_url='common:login')
def project_create(request):
    if request.method =='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.author = request.user 
            project.save()
            return redirect('main')
    else:
        form = ProjectForm()
    context={'form':form}
    return render(request, 'DS/project_form.html', context)
