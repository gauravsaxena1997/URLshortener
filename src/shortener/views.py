from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent
from .models import URL
from .forms import SubmitUrlForm

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		# bg_image = 'https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg'
		context = {
		    "title": "Submit URL",
		    "form": the_form,
		    # "bg_image": bg_image
		}
		return render(request, "shortener/home.html", context) 

	def post (self, request, *args, **kwargs):
		form  = SubmitUrlForm(request.POST)
		template = "shortener/home.html"
		if form.is_valid():
		    new_url = form.cleaned_data.get("url")
		    obj, created = URL.objects.get_or_create(url=new_url)
		    context = {
		        "object": obj,
		        "created": created,
		    }
		    if created:
		        template = "shortener/success.html"
		    else:
		        template = "shortener/already-exists.html"

		return render(request, template ,context)

class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		print(shortcode)
		qs = URL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() != 1 and not qs.exists():
		    raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)