#!/usr/bin/python
# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('test')


def todo_item(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home(request):
    return render(request, 'home.html')
# def login(request):


    # Create your views here.
