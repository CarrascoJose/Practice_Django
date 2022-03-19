from django.urls import path
from . import views


urlpatterns = [
    path('welcome/', views.index), #our-domain.com/myapp
    path('days/',views.show_days),
    path('days/<day_slug>/',views.specific_day,name='day-detail')
]