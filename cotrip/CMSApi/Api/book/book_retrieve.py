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
from datetime import datetime, timedelta



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
				q_dict["uuid"] = record[0].uuid
				q_dict["title"] = record[0].title
				q_dict["issued_date"] = record[0].issued_date
				q_dict["release_date"] = record[0].release_date
				if record[0].oversea == False:
					q_dict["oversea"] = str(0)
				else:
					q_dict['oversea'] = str(1)
				if record[0].draft ==str(0):
					q_dict["draft"] = "Unpublished"
				elif record[0].draft == str(1):
					q_dict["draft"] = "Editing"
				else:
					q_dict["draft"] = "Release"


				if record[0].series_code == None:
						series_name = None
				else :
					series_name = record[0].series_code.series_name

				if record[0].area_code == None:
						area_name = None
				else :
					area_name = record[0].area_code.area_name

				q_dict["series_code"] = series_name
				q_dict["area_code"] = area_name
				q_dict["book_type"] = record[0].book_type
				q_dict["paper_version"] = record[0].paper_version
				q_dict["expiration_start"] = record[0].expiration_start
				q_dict["item_code_android"] = record[0].item_code_android
				q_dict["item_code_ios"] = record[0].item_code_ios
				q_dict["expiration_end"] = record[0].expiration_end
				q_dict["explanation"] = record[0].explanation
				q_dict["free_url"] = record[0].free_url
				q_dict["map_credit"] = record[0].map_credit
				q_dict['expire_days'] = record[0].expire_days
				q_dict['thumbnailURL'] = record[0].thumbnailURL
				if record[0].modified !=None:
					m = record[0].modified+timedelta(hours=5,minutes=30)
					q_dict["modified"] =  m.strftime("%Y-%m-%d %I:%M %p")
				else:
					q_dict["modified"] = ''
				p = record[0].created+timedelta(hours=5,minutes=30)
				q_dict['registration'] = p.strftime("%Y-%m-%d %I:%M %p")


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