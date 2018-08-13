from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import URL


def redirect_view (request,shortcode=None, *args, **kwargs):
	
	obj  = get_object_or_404( URL,shortcode = shortcode)     #(class_name, field_name)

	# try:
	# 	obj = URL.objects.get(shortcode=shortcode)
	# except:	
	# 	obj = URL.objects.all().first()

	return HttpResponse ("{url} , {timestamp}".format(url=obj.url,timestamp=obj.timestamp))