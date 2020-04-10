import re
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from MappleApi.api_packages import *
from datetime import datetime
from django.db.models import Q
import os
from django.db.models import Max

#Serializer for api
from rest_framework import serializers
from Book.models import MstBooks

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstBooks
		fields = '__all__'


class BookCreationUpdation(APIView):
	"""
	Book Creation & Updation POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create & update book for cms.

		Data Post: {
			"id"                   : "1"(Send this key in update record case,else it is not required!!)
			"isbn_edition"		   : "saasdsadsadsa",
			"uuid"		           : 3424324,
			"title" 	           : "adasd",
			"issued_date"          : "2019-03-24"(Y-m-d)
			"release_date"		   : "2019-03-23",
			"expiration_start"     : "2019-03-24"(Y-m-d)
			"expiration_end"	   : "2019-03-23",
			"oversea"		       : "0",(1=oversea,0=domestic)
			"series_code"		   : "1",
			"area_code"		       : "1",
			"book_type" 	       : "were",
			"paper_version"        : "sfsfsd"
			"contents_version"	   : "dddddddddd",
			"item_code_android"    : "adasd",
			"item_code_ios"        : "sdadsa",
			"location"			   : ""
			"paper_enabled"        : 0
		    "map_enabled"          : 0
			"dl_map_enabled"       : 0
		    "station_enabled"      : 0
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
			data = request.data
			err_message = {}
			if "id" in data:
				unique_check = MstBooks.objects.filter(~Q(id=data["id"]),Q(uuid__iexact=data["uuid"]))
			else:
				unique_check = MstBooks.objects.filter(Q(uuid__iexact=data["uuid"]))
								
			if unique_check.count() != 0:
				err_message["unique_check"] = "Product Code with this name already exists!!"
			else:
				pass
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})


			if "id" in data:
				book_record = MstBooks.objects.filter(id=data['id'])
				if book_record.count() == 0:
					return Response(
					{
						"success": False,
	 					"message": "Book data is not valid to update!!"
					}
					)
				else:
					data["modified"] = datetime.now()
					book_serializer = \
					BookSerializer(book_record[0],data=data,partial=True)
					if book_serializer.is_valid():
						data_info = book_serializer.save()
					else:
						print("something went wrong!!")
						return Response({
							"success": False, 
							"message": str(book_serializer.errors),
							})
			else:
				book_serializer = BookSerializer(data=data)
				if book_serializer.is_valid():
					data_info = book_serializer.save()
				else:
					print("something went wrong!!")
					return Response({
						"success": False, 
						"message": str(book_serializer.errors),
						})
			final_result = []
			final_result.append(book_serializer.data)
			return Response({
						"success": True, 
						"message": "Book creation/updation api worked well!!",
						"data": final_result,
						})
		except Exception as e:
			print("Book creation/updation Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})
