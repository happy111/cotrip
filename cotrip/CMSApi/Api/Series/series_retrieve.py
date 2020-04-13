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
from Book.models import MstSeries
from MappleApi.api_packages import *
from datetime import datetime, timedelta




class SeriesRetrieve(APIView):
	"""
	Series retrieval POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for retrieval of Series data.

		Data Post: {
			"id"                   : "1"
		}

		Response: {

			"success": True, 
			"message": "Series retrieval api worked well!!",
			"data": final_result
		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			err_message = {}
			err_message["id"] = \
					validation_master_anything(data["id"],
					"Series Id",contact_re, 1)
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})
			record = MstSeries.objects.filter(id=data['id'])
			if record.count() == 0:
				return Response(
				{
					"success": False,
 					"message": "Provided Series data is not valid to retrieve!!"
				}
				)
			else:
				final_result = []
				q_dict = {}
				q_dict["id"] = record[0].id

				if record[0].oversea == False:
					q_dict["oversea"] = str(0)
				else:
					q_dict['oversea'] = str(1)				

				q_dict["series_name"] = record[0].series_name
				q_dict["sort"] = record[0].sort
				if record[0].draft ==str(0):
					q_dict["draft"] = "Unpublished"
				elif record[0].draft == str(1):
					q_dict["draft"] = "Editing"
				else:
					q_dict["draft"] = "Release"
				q_dict["revision"] = record[0].revision
				q_dict["series_code"] = record[0].series_code
				q_dict["status"] = record[0].status
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
							"message": "Series retrieval api worked well!!",
							"data": final_result,
							})
			else:
				return Response({
							"success": True, 
							"message": "No Series data found!!"
							})
		except Exception as e:
			print("Series retrieval Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})