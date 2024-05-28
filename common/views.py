from django.shortcuts import redirect, render
from django.contrib.auth import logout,authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('main')

def signup_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, exception):
    return render(request, 'common/404.html', {})

@login_required(login_url='common:login')
def profile_view(request):
    User=request.user
    context={'user':User}
    return render(request, 'common/profile.html', context)

@login_required(login_url='common:login')
def profile_create(request):
    User=request.user
    if request.method == "POST":
        User.profile=request.FILES.get('profileimage')
        print(request.FILES.get('profileimage'))
        User.save()
    context = {'user': User}
    return render(request, 'common/create_profile.html', context)
