from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse("Welcome")
    #return render(request,"Welcome!")

def view_article(request,id):
    text = "Displaying article Number: %s"%(id)
    return HttpResponse(text)

def view_articles(request, month, year):
    text = "Displaying articles of : %s/%s"%(year,month)
    return HttpResponse(text)

def show_days(request):
    day = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "myapp/index.html",{
        'show_days':True,
        'day':day,
        'daysOfWeeks':daysOfWeek
    }
    )

