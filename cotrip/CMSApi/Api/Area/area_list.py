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
from Book.models import MstAreas





class AreaList(APIView):
	"""
	Area Listing POST API
		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for listing of area.
	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			area_data = MstAreas.objects.filter().order_by('id')
			if area_data.count() > 0:
				pro_data =[]
				for i in area_data:
					if i.draft ==str(0):
						dr = "Unpublished"
					elif i.draft == str(1):
						dr = "Editing"
					else:
						dr = "Release"
					if i.oversea ==1:
						country = "Overseas"
					else:
						country = "Domestic"
					if i.status ==0:
						st = "Invalid"
					else:
						st = "Effectiveness"
					p_list ={}
					p_list['id'] = i.id
					p_list['oversea'] = country
					p_list['area_name'] = i.area_name
					p_list['sort'] = i.sort
					p_list['draft'] = dr
					p_list['revision'] = i.revision
					p_list['area_code'] = i.area_code
					p_list['status'] = st
					pro_data.append(p_list)
				return Response({"status":True,
								"data":pro_data})
			else:
				return Response({"status":True,
								"data":[]})
		except Exception as e:
			print("Area list Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})



