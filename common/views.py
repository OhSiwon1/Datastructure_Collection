from django.shortcuts import redirect, render
from django.contrib.auth import logout,authenticate, login
from common.forms import UserForm

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