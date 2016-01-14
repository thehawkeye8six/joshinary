from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /words/
	url(r'^$', views.index, name='index'),
	# ex: /words/5/
	url(r'^(?P<word_id>[0-9]+)/$', views.detail, name='detail'),
]
