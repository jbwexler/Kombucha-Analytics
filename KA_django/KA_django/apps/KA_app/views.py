from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    table = [x.data() for x in Brew.objects.all()]
    return HttpResponse(table)