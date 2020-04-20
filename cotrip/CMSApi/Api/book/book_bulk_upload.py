from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import re
from MappleApi.api_packages import *
import datetime
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from Book.models import *
from django.db.models import Q
import os
import xlrd 
from Configuration.models import Excelimport
import pandas as pd
from datetime import datetime
import math
from rest_framework import serializers
from PIL import Image
import pytesseract
from os import path



class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstBooks
		fields = '__all__'


class BookBulkUpload(APIView):
	"""
	Excel upload POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to Bulk registration for book.

		Data Post: {
				"image" : 'a.jpg'
		}
		Response: {

		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			mutable = request.POST._mutable
			request.POST._mutable = True
			rd = {}
			data = request.data
			allimages = list(data.values())
			for i in allimages:
				a = str(i)
				p = os.path.join(os.path.dirname(os.path.dirname(__file__)))
				x = p.replace("CMSApi/Api", "")
				f_path = x + str('media/epubcover/')
				epub = f_path+str(i)
				f_path = x + str('media/epub/')
				epubs = f_path+str(i)
				if os.path.exists(epub):
					os.remove(epub)
				else:
					pass
				if os.path.exists(epubs):
					os.remove(epubs)
				else:
					pass
				if a == 'null':
					pass
				else:
					fimage = a.split('.')
					if fimage[1] == str('epub'):
						rd['epub'] = i
					else:
						epubs = None
					if fimage[1] == str('jpg'):
						rd['epub_cover'] = i

					else:
						epubs_cover  = None
					epubs =  str('epub/')+str(fimage[0])+'.epub'
					epubs_cover =  str('epubcover/')+str(fimage[0])+'.jpg'
					bobj = MstBooks.objects.filter(Q(isbn_edition=fimage[0]) | Q(epub=epubs) | Q(epub_cover=epubs_cover))
					if bobj.count() > 0:
						rd["modified"] = datetime.now()
						book_serializer = BookSerializer(bobj[0],data=rd,partial=True)
						if book_serializer.is_valid():
							data_info = book_serializer.save()
						else:
							print("ccccccccccccccc",book_serializer.errors)
					else:
						book_serializer = BookSerializer(data=rd)
						if book_serializer.is_valid():
							data_info = book_serializer.save()
						else:
							print("ccccccccccccccc",book_serializer.errors)
					rd.clear()
			return Response({
					"success": True, 
					"message": "Book creation/updation api worked well!!",

					})
		except Exception as e:
			print("Book creation/updation Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})





