from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import re
from django.utils.html import strip_tags
from _thread import start_new_thread
from datetime import datetime
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
import json
from Book.models import MstBooks
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





class OneTimeBookList(APIView):
	"""
	Book Listing POST API
		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for listing of book.

		Data Post : {
	
						"isbn_edition":"",
						"book_name":"" ,
						"compaign_book" : "0", ( if checked ->"1" ,if not checked -> "0")
						"page_info":
									{
										"page_size":"10",
										"page_no":"1"
									}
						
					}

		Response: {

			"success": True, 
			"message": "Book creation/updation api worked well!!",
			"data": final_result
		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			book_data = MstBooks.objects.filter().order_by('id')
			if book_data.count() > 0:

				data = request.data

				title = ""
				if "book_name" in data:
					title = data["book_name"]
					if title != "" :
						book_data = book_data.filter(title__icontains=title)

				isbn_edition=""
				if "isbn_edition" in data:
					isbn_edition = data["isbn_edition"]
					if isbn_edition != "" :
						book_data = book_data.filter(isbn_edition__icontains=isbn_edition)

				if "compaign_book" in data:
					compaign_book = data["compaign_book"]

					if compaign_book == "0" : # It mean unchecked
						book_data = book_data.filter(~Q(series_code=None))


				page_no = 1
				page_size = 20
				if "page_info" in data:
					if "page_size" in data["page_info"] :
						page_size = int(data["page_info"]["page_size"])

					if "page_no" in data["page_info"] :
						page_no = int(data["page_info"]["page_no"])

				try:
					if page_size > 200:
						page_size = 200
					pages = Paginator(book_data, page_size)
					book_data_pages = pages.page(page_no)
				except PageNotAnInteger:
					page_no = 1
					book_data_pages = pages.page(page_no)
				except EmptyPage:
					page_no = pages.num_pages
					book_data_pages = pages.page(page_no)

				page_count = pages.count
				page_info = {
					"page_no": page_no,
					"page_size": page_size,
					"total_items": page_count,
				}
				pro_data =[]
				series_name = None
				for i in range(len(book_data_pages.object_list)):
					
					if book_data_pages[i].series_code == None:
						series_name = None
					else :
						series_name = book_data_pages[i].series_code.series_name
					p_list ={}
					p_list['id'] = book_data_pages[i].id
					p_list['series_name'] = series_name
					p_list['isbn_edition'] = book_data_pages[i].isbn_edition
					p_list['title'] = book_data_pages[i].title
					p_list['publication_date'] = book_data_pages[i].release_date
					p_list['download_deadline'] = book_data_pages[i].expiration_end
					pro_data.append(p_list)
				return Response({"status":True,"page": page_info,	
								"data":pro_data})
			else:
				return Response({"status":True,
								"data":[]})
		except Exception as e:
			print("Book list Api Stucked into exception!!")
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})