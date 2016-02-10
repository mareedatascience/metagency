from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is a list of stations (with pagination)")

def station(request, stn_num, fmt="html"):
	return HttpResponse("This is a page for {stn_num} in {fmt} format. It includes station metadata, a list of nearby stations, station climatology, list of products available".format(stn_num=stn_num, fmt=fmt))

def wx(request, stn_num, wx, fmt="html"):
	return HttpResponse("This is a page for {stn_num} and weather element {wx} in {fmt} format. It has a list of reporting frequencies available or the product itself in the default format".format(stn_num=stn_num, wx=wx, fmt=fmt))

def fx(request, stn_num, wx, fx, fmt="html"):
	return HttpResponse("This is a page for {stn_num} and weether element {wx} at reporting frequency {wx} in {fmt} format.".format(stn_num=stn_num, wx=wx, fx=fx, fmt=fmt))

def search(request, query, fmt="html"):
	return HttpResponse("This is a page to display search results for stations matching {query} displayed in {fmt} format".format(query=query, fmt=fmt))

def searchpage(request):
	return HttpResponse("This is a html page with a UI for station searches")

