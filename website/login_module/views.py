from django.shortcuts import render, redirect
from django.http import HttpResponse

def user(request, userid):
	context = {
	'userid' : userid
	}
	user_details = get_user_details(userid)
	context['username'] = user_details.user.username
	context['firstname'] = user_details.firstname
	context['lastname'] = user_details.lastname
	return render(request, 'user.html', context)