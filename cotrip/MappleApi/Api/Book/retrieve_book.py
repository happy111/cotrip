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
import os
from mapper import settings
from datetime import datetime, timedelta


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstBooks
		fields = '__all__'


def addr_set():
	domain_name = "http://172.105.41.233:8080media/"
	return domain_name

	
class RetrieveBook(APIView):
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
				            "id": 17,
				            "isbn_edition": "9784398286642-17-1",
				            "title": "ソウル’１９",
				            "issued_date": "2018-10-15",
				            "thumbnailURL": "http://172.105.41.233:1234/media/epubcover/9784398286642-17-1.jpg",
				            "download_url": "http://172.105.41.233:1234/media/epub/9784398286642-17-1.epub",
				            "description": "変化の激しいソウルの最旬&定番が満載の一冊。\\n何度でもオイシイ絶品焼肉、大流行チーズタッカルビ、激辛フード、ローカル&ディープな地元メシなど必食グルメが盛りだくさん。大本命の韓国コスメは新商品も続々&王道もバッチリ。",
				            "file_size": "5.29 MB"
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

				q_dict["id"] = record[0].id
				q_dict["isbn_edition"] = record[0].isbn_edition
				q_dict["title"] = record[0].title
				e = record[0].issued_date+timedelta(hours=5,minutes=30)
				q_dict['issued_date'] = e.strftime("%Y-%m-%d")
				domain_name = addr_set()
				full_path = domain_name + str(record[0].epub_cover)
				if full_path == 'http://172.105.41.233:1234/media/':
					q_dict['thumbnailURL'] = ''
				else:
					q_dict['thumbnailURL'] = full_path
				full_path_book = domain_name + str(record[0].epub)
				if full_path_book == 'http://172.105.41.233:8080/media/':
					q_dict['download_url'] = ''
				else:
					q_dict['download_url'] = full_path_book
				q_dict['description'] = record[0].explanation
				file_size = ""
				if record[0].epub != None:
					file = os.path.join(settings.BASE_DIR, 'media/{}'.format(str(record[0].epub)))
					file_size = round(os.stat(file).st_size/1000000,2)
					
				q_dict['file_size'] = str(file_size) + " MB"
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