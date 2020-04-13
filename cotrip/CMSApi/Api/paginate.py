from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(query,page):
	paginator = Paginator(query, 2)
	try:
		query = paginator.page(page)
	except PageNotAnInteger:
		query = paginator.page(1)
	except EmptyPage:
		query = paginator.page(paginator.num_pages)
	return query