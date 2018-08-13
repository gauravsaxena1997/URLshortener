import random
import string

def code_generator (size=6,chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
	new_code = code_generator(size=size)
	# print(instance)                                          #aws.com
	# print(instance.__class__)	    						   #<class 'shortener.models.URL'>
	# print(instance.__class__.__name__)                       #URL
	Klass = instance.__class__
	qs_exists = Klass.objects.filter(shortcode=new_code).exists()
	if qs_exists:                                            #when shortcode already exists in db
	    return create_shortcode(instance, size=size)         #whole fn will execute again
	return new_code