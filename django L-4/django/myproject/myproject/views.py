# from django.http import HttpResponse


from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'website/webIndex.html')
    # return render(request, 'index.html')
    # return HttpResponse("Welcome to the Home Page!")

 

from django.http import HttpResponse

def about(request):
    return HttpResponse("Welcome to the about Page!")

 

from django.http import HttpResponse

def contact(request):
    return HttpResponse("Welcome to the contact Page!")
