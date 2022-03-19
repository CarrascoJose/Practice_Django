from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return HttpResponse("Welcome")


def show_days(request):
    day = datetime.now().date()
    days = [{
        'name':'Monday',
        'time':'raining',
        'slug':'a-monday-day'
    },
    {
        'name':'Friday',
        'time':'sunny',
        'slug':'a-friday-day'
    }
    ]

    return render(request, "myapp/index.html",{
        'show_days':True,
        'day':day,
        'daysOfWeeks':days,

    }
    )

def specific_day(request,day_slug):
    print(day_slug)
    selected_day = {
        'title': 'A certain day',
        'description': 'This the day'
    }
    return render(request,"myapp/days.html",{
        'day_name':selected_day['title'],
        'day_description':selected_day['description']
    }
    
)

