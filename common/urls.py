from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/<int:user_id>', views.profile_view, name='profile'),
    path('create_profile/<int:user_id>', views.profile_create, name='profile_create'),
]

