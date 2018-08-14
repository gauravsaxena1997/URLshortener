from django.db import models

from shortener .models import URL


class ClickEventManager(models.Manager):
	def create_event(self, Instance):
		if isinstance(Instance, URL):
		    obj, created = self.get_or_create(url=Instance)
		    obj.count += 1
		    obj.save()
		    return obj.count
		return None

class ClickEvent(models.Model):
	url  	    = models.OneToOneField(URL)
	count       = models.IntegerField(default=0)
	updated     = models.DateTimeField(auto_now=True) 
	timestamp   = models.DateTimeField(auto_now_add=True)

	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)