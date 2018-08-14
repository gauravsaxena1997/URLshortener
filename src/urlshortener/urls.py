from django.conf.urls import url
from django.contrib import admin

from shortener.views import redirect_view, HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', redirect_view, name='shortcode'),
]
