from django.shortcuts import render,redirect
from .models import Project, Comment, Year, Hashtag
from DS.forms import ProjectForm, CommentForm,OldForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from makeit.models import Question
from django.db.models import Count
from django.db.models import Q
import logging
logger = logging.getLogger('croffle')

def group_checks(user):
    return user.groups.filter(name='can_make_proj').exists()

def group_check(user):
    return user.groups.filter(name='h_teacher').exists()

def videourl(img_element_url):
    video_id = img_element_url.split("/")[-1]
    video_id = video_id.split("v=")[-1].split("&")[0]
    embed_url = f"https://www.youtube.com/embed/{video_id}"
    return embed_url


# Create your views here.
def main(request):
    logger.info("INFO 레벨로 출력")
    year_list=[]
    for yea in Year.objects.all():
        year_list.append({'year':yea.year,'year_id':yea.id,'queryset':yea.project_set.annotate(like_count=Count('harts')).order_by('-like_count')[:3]})
    question_list=Question.objects.order_by()[:17]
    context1={'year_list':year_list,'question_list':question_list}
    return render(request, 'DS/main.html', context1)

def Hashtag_view(request,hashtag_id):
    hashtag= Hashtag.objects.get(id=hashtag_id)
    context={'hashtag':hashtag}
    return render(request,'DS/Hashtag.html',context)

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
@user_passes_test(group_checks, login_url='loginplz') #login_url= "<인증이 필요합니다.> 창"
def project_create(request):
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.author = request.user
            project.video = videourl(project.video)
            project.save()
            return redirect('main')
    else:
        form = ProjectForm()
    context={'form':form,'year_list':Year.objects.all(),'hashtag_list':Hashtag.objects.all()}
    return render(request, 'DS/project_form.html', context)

@login_required(login_url='common:login')
def project_modify(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.user != project.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('project_detail', project_id=project.id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    context = {'form': form, 'year_list':Year.objects.all(),'hashtag_list':Hashtag.objects.all(),'project':project}
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
    project.harts.add(request.user)
    return redirect('project_detail', project_id=project.id)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        comment.delete()
    return redirect('project_detail', project_id=comment.project.id)

def assignplz(request):
    return render(request,'DS/assignplz.html')

def Search_view(request):
    kw = request.GET.get('kw', '')  # 검색어
    project_list = Project.objects.order_by()
    if kw:
        project_list = project_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(author__username__icontains=kw)  # 질문 글쓴이 검색
        ).distinct()
    context = {'kw': kw,'project_list':project_list}
    return render(request, 'DS/search.html', context)

@login_required(login_url='common:login')
@user_passes_test(group_check, login_url='loginplz') #login_url= "<인증이 필요합니다.> 창"
def old_create(request):
    if request.method =='POST':
        form = OldForm(request.POST,request.FILES)
        if form.is_valid():
            oldproj=form.save(commit=False)
            oldproj.author = request.user
            oldproj.video = videourl(oldproj.video)
            oldproj.save()
    else:
        form = OldForm()
    context={'form':form,'year_list':Year.objects.all()}
    return render(request, 'DS/oldproj_form.html', context)

