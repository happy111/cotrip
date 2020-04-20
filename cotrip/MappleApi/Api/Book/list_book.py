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


def addr_set():
	domain_name = "http://172.105.41.233:1234/media/"
	return domain_name

class ListBook(APIView):
	"""
	Book Listing POST API
		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for listing of book.
	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			book_data = MstBooks.objects.filter().order_by('id')
			if book_data.count() > 0:
				pro_data =[]
				for i in book_data:
					p_list ={}
					p_list['id'] = i.id
					p_list['isbn_edition'] = i.isbn_edition
					p_list['title'] = i.title
					domain_name = addr_set()
					full_path = domain_name + str(i.epub_cover)
					if full_path == 'http://172.105.41.233:1234/media/':
						p_list['thumbnailURL'] = ''
					else:
						p_list['thumbnailURL'] = full_path
					full_path_book = domain_name + str(i.epub)
					if full_path_book == 'http://172.105.41.233:1234/media/':
						p_list['download_url'] = ''
					else:
						p_list['download_url'] = full_path_book
					p_list['description'] = i.explanation
					pro_data.append(p_list)
				return Response({"status":True,
								"data":pro_data})
			else:
				return Response({"status":True,
								"data":[]})
		except Exception as e:
			print("Book list Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})



