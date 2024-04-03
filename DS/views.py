from django.shortcuts import render,redirect
from .models import Project, Comment
from DS.forms import ProjectForm

# Create your views here.
def main(request):
    project_list = Project.objects.order_by()
    context = {'project_list':project_list}
    return render(request, 'DS/main.html', context)

def ProjectsByYears_view(request):
    project_list = Project.objects.order_by()
    context = {'project_list': project_list}
    return render(request,'DS/ProjectsByYears.html', context)

def detail_view(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'DS/project_detail.html', context)

def comments_create(request,project_id):
    project = Project.objects.get(id=project_id)
    comment = Comment(project=project, content=request.POST.get('content'))
    comment.save()
    return redirect('project_detail',project_id=project.id)

def project_create(request):
    if request.method =='POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.save()
            return redirect('main')
    else:
        form = ProjectForm()
    context={'form':form}
    return render(request, 'DS/project_form.html', context)
