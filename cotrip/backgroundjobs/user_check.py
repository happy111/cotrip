import requests
from django.contrib.auth.models import User

def user_creation():
	all_user = User.objects.all()
	response=requests.get("https://cotrip-web.signite.jp/api_users")
	user_data = response.json()
	for i in user_data:
		user_check = all_user.filter(username=str(i))
		if user_check.count() == 1:
			pass
		else:
			user_create = User.objects.create_user(
						username=str(i),
						password="!!!!!!",
						is_staff=False,
						is_active=True
						)
	return "User check and registration successsful!!"