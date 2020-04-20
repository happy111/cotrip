from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import re
from rest_framework.permissions import IsAuthenticated
from MappleApi.api_packages import *
import json
from datetime import datetime
#Serializer for api
from rest_framework import serializers
from Book.models import MstBooks



class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstBooks
		fields = '__all__'


def addr_set():
	domain_name = "http://172.105.41.233:1234/media/"
	return domain_name

	
class OneTimeBookRetrieve(APIView):
	"""
	Book retrieval POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for retrieval of Book data.

		Data Post: {
			"id"                   : "1"
		}

		Response: {

			"success": True, 
			"message": "Book retrieval api worked well!!",
			"data": [
				        {
				            "id": 21,
				            "series_name": null,
				            "isbn_edition": "22222",
				            "title": "test2",
				            "publication_date": "2020-04-23",
				            "download_deadline": "2020-04-23"
				        }
    ]
 		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			err_message = {}
			err_message["id"] = \
					validation_master_anything(data["id"],
					"Book Id",contact_re, 1)
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})
			record = MstBooks.objects.filter(id=data['id'])
			if record.count() == 0:
				return Response(
				{
					"success": False,
 					"message": "Provided Book data is not valid to retrieve!!"
				}
				)
			else:
				final_result = []
				q_dict = {}

				if record[0].series_code == None:
						series_name = None
				else :
					series_name = record[0].series_code.series_name

				q_dict["id"] = record[0].id
				q_dict["series_name"] = series_name
				q_dict["isbn_edition"] = record[0].isbn_edition
				q_dict["title"] = record[0].title
				q_dict["publication_date"] = record[0].release_date
				q_dict["download_deadline"] = record[0].expiration_end

				domain_name = addr_set()
				if record[0].epub_cover != None:
					full_path = domain_name + str(record[0].epub_cover)
					q_dict['epub_cover'] = full_path 
				else:
					q_dict['epub_cover'] = ''
				
				final_result.append(q_dict)

			if final_result:
				return Response({
							"success": True, 
							"message": "Book retrieval api worked well!!",
							"data": final_result,
							})
			else:
				return Response({
							"success": True, 
							"message": "No Book data found!!"
							})
		except Exception as e:
			print("Book retrieval Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})