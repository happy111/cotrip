from django.urls import path, include
from MappleApi.Api.Authorization.register import Profile
from MappleApi.Api.Authorization.auth import Logout,Login
from MappleApi.Api.Authorization.registeruser import Signup
from MappleApi.Api.Authorization.change_pass import CpassWord
from MappleApi.Api.Book.list_book import ListBook 
from MappleApi.Api.Book.retrieve_book import RetrieveBook 



urlpatterns = [
	path('customer/signup_signin/',Signup.as_view()),
	path('customer/profile/',Profile.as_view()),
	path('customer/logout/',Logout.as_view()),
	path('customer/sigin/',Login.as_view()),
	path('customer/cpass/',CpassWord.as_view()),

	# Book List
	path('book/list/',ListBook.as_view()),
	path('book/retrieve/',RetrieveBook.as_view()),

]

