from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(requst):
    return render(requst, 'abaut/about.html')