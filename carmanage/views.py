import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test_view(request):
    return HttpResponse("have a nice day, this is a test page")