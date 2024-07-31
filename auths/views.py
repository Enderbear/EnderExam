from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 替换为你的主页URL
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # 替换为登录页面的URL

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账户创建成功，欢迎 {username}！')
            return redirect('login')  # 替换为登录页面的URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')