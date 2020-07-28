from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): # this is the view created for index.
    return render(request, 'pages/index.html') # step8.8

def about(request): # step 8.7
    return render(request, 'pages/about.html') # step 8.8