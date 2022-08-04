from django.http import HttpResponse
from django.shortcuts import render



def homePage(request):
    # return HttpResponse("Home Page")
    return render(request,'homepage.html')

def about(request):
    # return HttpResponse("About page")
    return render(request,'about.html')