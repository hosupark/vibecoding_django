from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def register_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, '회원가입이 완료되었습니다.')
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			messages.success(request, '로그인 성공!')
			return redirect('home')
		else:
			messages.error(request, '로그인 정보가 올바르지 않습니다.')
	else:
		form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})

def logout_view(request):
	logout(request)
	messages.info(request, '로그아웃 되었습니다.')
	return redirect('home')

# Create your views here.
