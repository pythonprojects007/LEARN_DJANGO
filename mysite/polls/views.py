from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request)
    print("..............................................")
    return HttpResponse("Hello you are in the polls index")

 


 