from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from shortener.views import URLRedirectView, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='shortcode'),	
]

if settings.DEBUG:
	urlpatterns+= ( static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) )