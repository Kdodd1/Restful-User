from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users$', views.index),
	url(r'^users/new$', views.new),
	url(r'^create$', views.create),
	url(r'^users/(?P<number>\d+$)',views.show),
	url(r'^users/(?P<number>\d+)/edit$', views.edit),
	url(r'^(?P<number>\d+)/update$', views.update),
	url(r'^(?P<number>\d+)/delete$', views.delete),
	url(r'^users/(?P<number>\d+)/delete$', views.delete)
	]