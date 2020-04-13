	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			if data['search'] !='':
				book_data = MstBooks.objects.filter(Q(isbn_edition__icontains=search)|Q(title__icontains=search))
			else:
				book_data = MstBooks.objects.filter().order_by('id')
			q_count = book_data.count()
			page_count = math.ceil((q_count/2))
			page = data['page']
			paged_query = pagination(book_data,page)
			pro_data = []
			for i in paged_query:
					p_list ={}
					p_list['id'] = i.id
					# p_list['series_name'] = series_name
					p_list['isbn_edition'] = i.isbn_edition
					p_list['title'] = i.title
					p_list['publication_date'] = i.release_date
					p_list['download_deadline'] = i.expiration_end
					pro_data.append(p_list)

			return Response({"status":True,	
							"page_count" : page_count,
							"data":pro_data})

		except Exception as e:
			print("Book list Api Stucked into exception!!")
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})