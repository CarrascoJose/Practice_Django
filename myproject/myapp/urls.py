from django.urls import path
from . import views


urlpatterns = [
    path('welcome/', views.index), #our-domain.com/myapp
    path('article/<int:id>/',views.view_article),
    path('article/<int:month>/<int:year>/',views.view_articles),
    path('days/',views.show_days)
]