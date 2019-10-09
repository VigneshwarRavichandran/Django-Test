from django.shortcuts import render, redirect
from django.http import HttpResponse
from .helper import *

def login(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		error = None
		if user_exists(username):
			valid_user = valid_credentials(username, password)
			if valid_user:
				userid = valid_user.id
				return redirect(user, userid)
			else:
				error = 'Invalid password'
		else:
			error = 'Invalid username'
		context['error'] = error
		return render(request, 'login.html', context)
	return render(request, 'login.html', context)

def register(request):
	context = {
		'error' : None,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		firstname = request.POST.get('firstname')
		lastname = request.POST.get('lastname')
		if not user_exists(username):
			create_user(username, password, firstname, lastname)
			return redirect(login)
		context['error'] = 'Username already exists'
		return render(request, 'register.html', context)
	return render(request, 'register.html', context)