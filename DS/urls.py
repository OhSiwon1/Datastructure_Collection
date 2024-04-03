from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('byyears/',views.ProjectsByYears_view, name='byyears'),
    path('<int:project_id>/', views.detail_view, name='project_detail'),
    path('create/<int:project_id>/', views.comments_create,name='comments_create'),
    path('project/create/', views.project_create, name='project_create'),

]

