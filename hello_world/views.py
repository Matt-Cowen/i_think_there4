from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == "POST":
       return HttpResponse("You POSTed something")
    else:
        return HttpResponse(str(request.method))