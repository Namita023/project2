from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome(request):
    return HttpResponse('<h1 style="background-color:red; color:yellow"><marquee>Welcome to this page.......</marquee></h1>')

def bye(request):
    return HttpResponse('<h1 style="color:blue"><marquee style="background-color:gray">Leaving this page.......</marquee></h1>')