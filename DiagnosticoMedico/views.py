from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("En este espacio son las citas medicas" )
