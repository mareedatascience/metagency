from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is a list of stations (with pagination)")

def station(request, stn_num):
	return HttpResponse("This is a page for {stn_num}. It includes station metadata, a list of nearby stations, station climatology, list of products available".format(stn_num=stn_num))

def wx(request, stn_num, wx):
	return HttpResponse("This is a page for {stn_num} and weather element {wx}. It has a list of reporting frequencies available or the product itself in the default format".format(stn_num=stn_num, wx=wx))

