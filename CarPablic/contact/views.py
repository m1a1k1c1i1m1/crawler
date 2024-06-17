from django.shortcuts import render

# Create your views here.


def contact(requst):
    return render(requst, 'contact\contact.html')
