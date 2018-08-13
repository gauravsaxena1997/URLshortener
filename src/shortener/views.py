from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import URL

def redirect_view (request,shortcode=None, *args, **kwargs):
	obj  = get_object_or_404( URL,shortcode = shortcode)     #(class_name, field_name)
	# return HttpResponse ("{url}".format(url=obj.url))
	return HttpResponseRedirect(obj.url)