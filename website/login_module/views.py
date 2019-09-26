from django.shortcuts import render, redirect
from django.http import HttpResponse

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