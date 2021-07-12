from django import http
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    #return HttpResponse("hello world")
    return render(request, "first_page.html")