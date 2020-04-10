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


class BookImport(APIView):
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
			data = request.data
			err_message = {}
			chk_ext =  str(data["image"])
			a = chk_ext.split('.')
			ext = a[1]
			if ext != 'tsv':
				return Response({
						"success": False, 
						"message" : "Only tsv is allowed" 
						})
			else:
				pass
			registration_data = {}
			alldata = Excelimport.objects.create(image=data['image'])
			dt = Excelimport.objects.filter(id=alldata.id)[0].image
			a = os.path.join(os.path.dirname(os.path.dirname(__file__)))
			b = a.replace("CMSApi/Api","")
			ad =b+'media/'+str(dt)
			tsv_read = pd.read_csv(ad, sep='\t')
			

			final_result = []
			uuid_d=tsv_read['[uuid]']
			name = tsv_read['[publication name]']
			issdate = tsv_read['[issue date]']
			reldate = tsv_read['[release date]']
			isbn = tsv_read['[ISBN]']
			edition = tsv_read['[edition]']
			printq = tsv_read['[print]']
			sereiscode = tsv_read['[series code]']



			areacode = tsv_read['[area code]']
			country = tsv_read['[country (domestic:? | overseas: ?)]']
			booktype = tsv_read['[Type (QR book / Sales book:? | QR book:? | Sales book:? | Free book:? | Free URL book :?)]']
			itemcodeios = tsv_read['[iOS item code]']
			itemcodeandroid = tsv_read['[Android item code]']
			expirestart = tsv_read['[Acquisition expiration start date]']
			expireend = tsv_read['[Acquisition expiration date]']
			expiredays = tsv_read['[Viewing expiration]']
			freeurl = tsv_read['[URL]']
			paper_version_d = tsv_read['[Paper version]']
			explanation_d = tsv_read['[Book description]']
			map_credit_d = tsv_read['[Credit]'] 
			

			for i in range(2,len(uuid_d)):
				if type(issdate[i])==str : 
					issdate1 = datetime.strptime(str(issdate[i]), "%Y/%m/%d" )
					issdate2 = issdate1.strftime("%Y-%m-%d")
				if type(reldate[i])==str:
					reldate1 = datetime.strptime(str(reldate[i]), "%Y/%m/%d" )
					reldate2 = reldate1.strftime("%Y-%m-%d")
				if type(expirestart[i]==str):
					expirestart1 = datetime.strptime(str(expirestart[i]), "%Y/%m/%d" )
					expirestart2 = expirestart1.strftime("%Y-%m-%d")
				if type(expireend[i]==str):
					expireend1 = datetime.strptime(str(expireend[i]), "%Y/%m/%d" )
					expireend2 = expireend1.strftime("%Y-%m-%d")


				if (type(expiredays[i])==float): # to identify the Nan value
					expiredays[i]=0

				

				series_code=None
				if(type(sereiscode[i])!=float):  # to identify the Nan value
					series =MstSeries.objects.filter(series_code=sereiscode[i])
					if series.count() == 0:
						err_message["unique_check"] = "Series code not exist in Series table"
					else:
						series_code=series[0].id
				

				
				area_code=None
				if(type(areacode[i])!=float):  # to identify the Nan value
					area = MstAreas.objects.filter(area_code=areacode[i])
					if area.count() == 0:
						err_message["unique_check"] = "Area code not exist in Area table"
					else:
						area_code=area[0].id

				

				data = {'uuid':int(uuid_d[i]),
						'issued_date':issdate2,
						'release_date':reldate2,
						'title':name[i],
						'isbn_edition':str(str(isbn[i])+"-"+str(edition[i])+"-"+str(printq[i])),
						'series_code': series_code,
						'area_code':area_code,
						'book_type':str(booktype[i]),
						'item_code_ios':itemcodeios[i],
						'item_code_android':itemcodeandroid[i],
						'expiration_start':expirestart2,
						'expiration_end':expireend2,
						'free_url':freeurl[i],
						'expire_days': int(expiredays[i]),
						'paper_version':paper_version_d[i],
						'explanation':explanation_d[i],
						'map_credit':map_credit_d[i],
						'draft':0,
						'oversea':country[i]
						}


				err_message = {}


				book_serializer = BookSerializer(data=data)
				if book_serializer.is_valid():
					data_info = book_serializer.save()
				else:
					print("something went wrong!!")
					return Response({
						"success": False, 
						"message": str(book_serializer.errors),
						})
			
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































