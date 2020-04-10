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

import os
import xlrd 
from Configuration.models import Excelimport
import pandas as pd
from datetime import datetime
import math
from rest_framework import serializers


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
				if a == 'null':
					pass
				else:
					fimage = a.split('.')
					if fimage[1] == str('epub'):
						rd['epub'] = i
					else:
						pass
					if fimage[1] == str('jpg'):
						rd['epub_cover'] = i
					else:
						pass
					bobj = MstBooks.objects.filter(isbn_edition=fimage[0])
					if bobj.count() > 0:
						rd["modified"] = datetime.now()
						book_serializer = BookSerializer(bobj[0],data=rd,partial=True)
						if book_serializer.is_valid():
							data_info = book_serializer.save()
						else:
							print("ccccccccccccccc",book_serializer.errors)
					else:
						pass
					rd.clear()
			return Response({
					"success": True, 
					"message": "Book creation/updation api worked well!!",

					})
		except Exception as e:
			print("Book creation/updation Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})





