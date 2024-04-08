from django.shortcuts import render,redirect
from .models import Project, Comment, Year
from DS.forms import ProjectForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def main(request):
    year1=Year.objects.get(id=1).project_set.order_by('-harts')
    year2=Year.objects.get(id=2).project_set.order_by('-harts')
    year3=Year.objects.get(id=3).project_set.order_by('-harts')[:3]
    context1={'year1':year1,'year2':year2,'year3':year3}
    return render(request, 'DS/main.html', context1)


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

@login_required(login_url='common:login')
def project_modify(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.user != project.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('project_detail', project_id=project.id)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    context = {'form': form, 'project':project}
    return render(request, 'DS/project_form.html', context)

@login_required(login_url='common:login')
def project_delete(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user != project.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('project_detail', project_id=project.id)
    project.delete()
    return redirect('main')

@login_required(login_url='common:login')
def project_vote(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.user == project.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        project.harts.add(request.user)
    return redirect('project_detail', project_id=project.id)
