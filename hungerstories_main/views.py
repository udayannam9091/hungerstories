from django.shortcuts import render
from django.http import HttpResponse


def home(req):
    return HttpResponse('<h1>This is homepage</h1>')