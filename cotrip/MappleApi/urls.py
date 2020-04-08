from django.urls import path, include
from MappleApi.Api.Authorization.register import Profile
from MappleApi.Api.Authorization.auth import Logout
from MappleApi.Api.Authorization.registeruser import Signup



urlpatterns = [
	path('customer/signup_signin/',Signup.as_view()),
	path('customer/profile/',Profile.as_view()),
	path('customer/logout/',Logout.as_view()),

]


