from django.db import models

class URL(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=15, unique=True)  #By Default null=False, blank=False
	# shortcode = models.CharField(max_length=15, default='shortcode')
	

	def __str__(self):
		return str(self.url)