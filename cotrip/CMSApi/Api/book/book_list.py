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
from datetime import datetime, timedelta


# def addr_set():
# 	domain_name = "http://172.105.41.233:1234/media/"
# 	return domain_name


def addr_set():
	domain_name = "http://192.168.0.17:1234/media/"
	return domain_name

class BookList(APIView):
	"""
	Book Listing POST API
		Authentication Required		: Yes
		Data Post : {				
								"search":"97",
								"page_no":"1"
											
					}

		Response: {

			"success": True, 
			"page": {
				        "page_no": 1,
				        "page_size": 10,
				        "total_items": 4,
				        "total_pages": 1
				    },
			"data": final_result
		}

		Service Usage & Description	: This Api is used for listing of book.
	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			book_data = MstBooks.objects.filter().order_by('id')
			if book_data.count() > 0:
				data = request.data
				pro_data =[]
				search = ""
				if "search" in data:
					search = data["search"]
					if search != "" :
						book_data = book_data.filter(Q(isbn_edition__icontains=search)|Q(title__icontains=search))
				page_no = 1
				page_size = 20
				if "page_size" in data :
					page_size = int(data["page_size"])
				if "page_no" in data :
					page_no = int(data["page_no"])
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
					"total_pages" : pages.num_pages
				}
				for i in range(len(book_data_pages.object_list)):
					if book_data_pages[i].draft ==str(0):
						dr = "Unpublished"
					elif book_data_pages[i].draft == str(1):
						dr = "Editing"
					else:
						dr = "Release"
					if book_data_pages[i].oversea ==str(0):
						country = "Overseas"
					else:
						country = "Domestic"
					if book_data_pages[i].status ==0:
						st = "Invalid"
					else:
						st = "Effectiveness"
					p_list ={}
					b = book_data_pages[i].isbn_edition
					ec = book_data_pages[i].epub_cover
					if b != None  and ec !='':
						if b != '':
							p_list['id'] = book_data_pages[i].id
							p_list['isbn_edition'] = book_data_pages[i].isbn_edition
							p_list['title'] = book_data_pages[i].title
							p_list['oversea'] = country
							m = book_data_pages[i].release_date+timedelta(hours=5,minutes=30)
							p_list['release_date'] = m.strftime("%Y-%m-%d")
				
							e = book_data_pages[i].issued_date+timedelta(hours=5,minutes=30)
							p_list['issued_date'] = e.strftime("%Y-%m-%d")
							
							if book_data_pages[i].modified !=None:
								p = book_data_pages[i].modified+timedelta(hours=5,minutes=30)
								p_list['modified'] = p.strftime("%Y-%m-%d")
							else:
								p_list['modified'] =''
							p_list['draft'] = dr
							p_list['status'] = st
							domain_name = addr_set()
							full_path = domain_name + str(book_data_pages[i].epub_cover)
							if full_path == 'http://172.105.41.233:1234/media/':
								p_list['epub_cover'] = ''
							else:
								p_list['epub_cover'] = full_path
							pro_data.append(p_list)
						else:
							pass
					else:
						pass
				return Response({"status":True,
								  "page": page_info,
								"data":pro_data})
			else:
				return Response({"status":True,
								"data":[]})
		except Exception as e:
			print("Book list Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})



	