from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDIECT_URL = getattr(settings, 'DEFAULT_REDIECT_URL', 'http://www.stubyurl.com')

def wildcard_redirect(request, path=None):
	new_url = DEFAULT_REDIECT_URL
	if path is not None:
		new_url = DEFAULT_REDIECT_URL + '/' + path
	return HttpResponseRedirect(new_url)