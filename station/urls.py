from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^([0-9]{4,6})/(.*)', views.wx, name='wx'),
	url(r'^([0-9]{4,6})$', views.station, name='station'),
    url(r'^$', views.index, name='index'),
]