from django.urls import path

from . import views

app_name = 'makeit'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'), 
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/', views.question_vote, name='question_vote'),

]