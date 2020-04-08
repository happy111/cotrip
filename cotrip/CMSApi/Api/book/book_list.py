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




class BookList(APIView):
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
					if i.draft ==str(0):
						dr = "Unpublished"
					elif i.draft == str(1):
						dr = "Editing"
					else:
						dr = "Release"
					if i.oversea ==str(0):
						country = "Overseas"
					else:
						country = "Domestic"
					if i.status ==0:
						st = "Invalid"
					else:
						st = "Effectiveness"

					p_list ={}
					p_list['id'] = i.id
					p_list['isbn_edition'] = i.isbn_edition
					p_list['title'] = i.title
					p_list['oversea'] = country
					p_list['release_date'] = i.release_date
					p_list['issued_date'] = i.issued_date
					p_list['modified'] = i.modified
					p_list['draft'] = dr
					p_list['status'] = st
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



