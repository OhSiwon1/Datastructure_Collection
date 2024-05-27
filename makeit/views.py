from django.shortcuts import render, redirect
from .models import Question, Answer
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator  
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw1', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw1': kw}
    return render(request, 'makeit/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'makeit/question_detail.html', context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('makeit:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'makeit/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('makeit:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'makeit/question_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    print(answer_id)
    answer = Answer.objects.get(id=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('makeit:detail', question_id=answer.question.id)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    project = Question.objects.get(id=question_id)
    if request.user != project.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('project_detail', question_id=project.id)
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('makeit:detail', question_id=project.id)
    else:
        form = QuestionForm(instance=project)
    context = {'form': form,'question':project}
    return render(request, 'makeit/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    project = Question.objects.get(pk=question_id)
    if request.user != project.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('project_detail', question_id=project.id)
    project.delete()
    return redirect('main')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    project = Question.objects.get(pk=question_id)
    project.voter.add(request.user)
    return redirect('makeit:detail', question_id=project.id)

