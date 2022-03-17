from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Welcome")
    #return render(request,"Welcome!")

def view_article(request,id):
    text = "Displaying article Number: %s"%(id)
    return HttpResponse(text)
    #return render(request,text)

def view_articles(request, month, year):
    text = "Displaying articles of : %s/%s"%(year,month)
    return HttpResponse(text)

