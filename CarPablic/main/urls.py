from django.urls import path
from . import views
from about.views import about
from contact.views import contact



urlpatterns = [
    path('', views.index ),
    path('about', about),
    path('Contact', contact)
    
]