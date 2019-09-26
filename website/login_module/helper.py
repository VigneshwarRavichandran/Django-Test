from .models import *	

def get_user_details(userid):
	user_details = UserDetails.objects.get(user_id=userid)
	return user_details