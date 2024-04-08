from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('byyears/<int:year_id>/',views.ProjectsByYears_view, name='byyears'),
    path('<int:project_id>/', views.detail_view, name='project_detail'),
    path('create/<int:project_id>/', views.comments_create,name='comments_create'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/modify/<int:project_id>/', views.project_modify, name='project_modify'),
    path('project/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    path('project/vote/<int:project_id>/', views.project_vote, name='project_vote'),

]

