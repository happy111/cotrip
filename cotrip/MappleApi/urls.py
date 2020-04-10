from django.urls import path, include
from MappleApi.Api.Authorization.register import Profile
from MappleApi.Api.Authorization.auth import Logout
from MappleApi.Api.Authorization.registeruser import Signup
from MappleApi.Api.Authorization.change_pass import CpassWord
from MappleApi.Api.Book.list_book import ListBook



urlpatterns = [
	path('customer/signup_signin/',Signup.as_view()),
	path('customer/profile/',Profile.as_view()),
	path('customer/logout/',Logout.as_view()),
	path('customer/cpass/',CpassWord.as_view()),

	# Book List
	path('book/list/',ListBook.as_view()),

]


