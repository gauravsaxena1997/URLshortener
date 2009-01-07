from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import URL


class HomeView(View):
	def get(self, request, *args, **kwargs):
		# the_form = SubmitUrlForm()
		# bg_image = 'https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg'
		# context = {
		#     "title": "Kirr.co",
		#     "form": the_form,
		#     "bg_image": bg_image
		# }
		return render(request, "shortener/home.html") 

	def post (self, request, *args, **kwargs):
		print (request.POST)                               #dict = {}
		print (request.POST.get('url'))                    #dict.get('url')
		# print (request.POST['url'])                		   #dict(['url'])
		return render(request, "shortener/home.html") 

def redirect_view (request,shortcode=None, *args, **kwargs):
	obj  = get_object_or_404( URL,shortcode = shortcode)     #(class_name, field_name)
	# return HttpResponse ("{url}".format(url=obj.url))
	return HttpResponseRedirect(obj.url)