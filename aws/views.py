from django.http import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request,'index.html')

    