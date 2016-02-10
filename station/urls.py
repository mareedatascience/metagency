from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^search/(.+)/([html|json|csv|pdf]*)', views.search, name='search'),
	url(r'^search', views.searchpage, name='searchpage'),
	url(r'^([0-9]{4,6})/(.+)/(.+)/([html|json|csv|pdf]*)', views.wx, name='fx'),
	url(r'^([0-9]{4,6})/(.+)/([html|json|csv|pdf]*)', views.wx, name='wx'),
	url(r'^([0-9]{4,6})/([html|json|csv|pdf]*)$', views.station, name='station'),
    url(r'^$', views.index, name='index'),
]
