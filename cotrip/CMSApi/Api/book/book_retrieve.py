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


class BookRetrieve(APIView):
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
				q_dict["id"] = record[0].id
				q_dict["isbn_edition"] = record[0].isbn_edition
				q_dict["product_code"] = record[0].product_code
				q_dict["title"] = record[0].title
				q_dict["issued_date"] = record[0].issued_date
				q_dict["release_date"] = record[0].release_date
				q_dict["oversea"] = record[0].oversea
				q_dict["series_code"] = record[0].series_code
				q_dict["area_code"] = record[0].area_code
				q_dict["book_type"] = record[0].book_type
				q_dict["paper_version"] = record[0].paper_version
				q_dict["contents_version"] = record[0].contents_version
				q_dict["item_code_android"] = record[0].item_code_android
				q_dict["item_code_ios"] = record[0].item_code_ios
				q_dict["paper_enabled"] = record[0].paper_enabled
				q_dict["map_enabled"] = record[0].map_enabled
				q_dict["dl_map_enabled"] = record[0].dl_map_enabled
				q_dict["station_enabled"] = record[0].station_enabled
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