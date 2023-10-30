from django.http.response import HttpResponse
from django.shortcuts import render


def index():
    return HttpResponse("ola mundo!")