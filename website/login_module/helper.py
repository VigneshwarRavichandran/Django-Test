from .models import *	

def valid_credentials(username, password):
	user = Users.objects.get(username=username)
	if user.password == password:
		return user
	return False