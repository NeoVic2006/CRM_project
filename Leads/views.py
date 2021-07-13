from django import http
from django.http.response import HttpResponseForbidden
from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead

# Create your views here.


def leads_page(request):

    leads = Lead.objects.all()

    context = {
        "Leads": leads,
    }

    #return HttpResponse("hello world")
    return render(request, "leads_page.html", context)