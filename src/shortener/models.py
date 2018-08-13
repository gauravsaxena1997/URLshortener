from django.db import models

class URL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode 	= models.CharField(max_length=15, unique=True)  #By Default null=False, blank=False
	# shortcode = models.CharField(max_length=15, default='shortcode')
	updated 	= models.DateTimeField(auto_now=True)	   #everytime the model is saved
	timestamp 	= models.DateTimeField(auto_now_add=True)  #when model was created
	# empty_timestamp 	= models.DateTimeField(auto_now_add=False,auto_now=False)  #empty

	def __str__(self):
		return str(self.url)