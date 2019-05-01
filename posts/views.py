from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
  return HttpResponse('Hello from posts!')

def anything(request):
  print(request.body)
  return HttpResponse('Hello! ' + str(request))