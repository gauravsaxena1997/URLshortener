from django.conf.urls import url
from django.contrib import admin

from shortener.views import redirect_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<shortcode>[\w-]+)/$', redirect_view),
]
