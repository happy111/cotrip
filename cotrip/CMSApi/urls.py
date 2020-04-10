from django.urls import path, include
from CMSApi.Api.Authorization.auth import Logout,SignIn

# Area part
from CMSApi.Api.Area.areas_create_update import AreaCreationUpdation
from CMSApi.Api.Area.area_list import AreaList
from CMSApi.Api.Area.area_retrieve import AreaRetrieve

# Series part
from CMSApi.Api.Series.series_create_update import SeriesCreationUpdation
from CMSApi.Api.Series.series_list import SeriesList
from CMSApi.Api.Series.series_retrieve import SeriesRetrieve


# Book part
from CMSApi.Api.book.book_create_update import BookCreationUpdation
from CMSApi.Api.book.book_list import BookList
from CMSApi.Api.book.book_retrieve import BookRetrieve
from CMSApi.Api.book.book_import import BookImport

# One time url part

from CMSApi.Api.One_time_url.one_time_book_list import OneTimeBookList
from CMSApi.Api.One_time_url.one_time_book_retrieve import OneTimeBookRetrieve

urlpatterns = [
	path('signin/',SignIn.as_view()),
	path('logout/',Logout.as_view()),

	#Area Module
	path('area/create_update/',AreaCreationUpdation.as_view()),
	path('area/list/',AreaList.as_view()),
	path('area/retrieve/',AreaRetrieve.as_view()),


	#Series Module
	path('series/create_update/',SeriesCreationUpdation.as_view()),
	path('series/list/',SeriesList.as_view()),
	path('series/retrieve/',SeriesRetrieve.as_view()),



	#Book Module
	path('book/create_update/',BookCreationUpdation.as_view()),
	path('book/list/',BookList.as_view()),
	path('book/retrieve/',BookRetrieve.as_view()),
	path('book/import/',BookImport.as_view()),

	#One time url Module
	path('one_time_url/book/list/',OneTimeBookList.as_view()),
	path('one_time_url/book/retrieve/',OneTimeBookRetrieve.as_view()),
]


