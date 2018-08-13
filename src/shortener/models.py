from django.db import models

from .utils import code_generator, create_shortcode

class URL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True, blank=True)  
	#By Default null=False, blank=False
	# shortcode = models.CharField(max_length=15, default='shortcode')
	updated 	= models.DateTimeField(auto_now=True)	   #everytime the model is saved
	timestamp 	= models.DateTimeField(auto_now_add=True)  #when model was created
	# empty_timestamp 	= models.DateTimeField(auto_now_add=False,auto_now=False)  #empty

	def __str__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		#       if not "http" in self.url:
		#           self.url = "http://" + self.url
		super(URL, self).save(*args, **kwargs)