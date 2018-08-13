from django.db import models

from .utils import code_generator, create_shortcode


class URLManager(models.Manager):
	# URL.objects.all()
	def all(self, *args, **kwargs):
		qs_main = super(URLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	# URL.objects.refresh_shortcodes()
	def refresh_shortcodes(self):
		qs = URL.objects.filter(id__gte=1)
		# if items is not None and isinstance(items, int):
		#     qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
		    q.shortcode = create_shortcode(q)
		    # print(q.shortcode)
		    # print(q.id)
		    q.save()
		    new_codes += 1
		return "New codes made: {i}".format(i=new_codes)


class URL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True, blank=True)  
	#By Default null=False, blank=False
	# shortcode = models.CharField(max_length=15, default='shortcode')
	updated 	= models.DateTimeField(auto_now=True)	   #everytime the model is saved
	timestamp 	= models.DateTimeField(auto_now_add=True)  #when model was created
	# empty_timestamp 	= models.DateTimeField(auto_now_add=False,auto_now=False)  #empty
	active = models.BooleanField(default=True)

	objects = URLManager()
	abc = URLManager()

	def __str__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		#       if not "http" in self.url:
		#           self.url = "http://" + self.url
		super(URL, self).save(*args, **kwargs)