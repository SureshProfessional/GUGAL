from django.shortcuts import render
from .models import *


def index(request):    
    pardada = Son_of_jivadada.objects.all()
    dada = Son_of_dada.objects.all()
    uncle = Son_of_uncle.objects.all()

    context = {'pardada':pardada,
               'dada':dada,
               'uncle':uncle,
               }
    
    return render(request,"index.html",context)


def addname(request):
    pardada = Son_of_jivadada.objects.all()
    dada = Son_of_dada.objects.all()
    uncle = Son_of_uncle.objects.all()

    context = {'pardada':pardada,
               'dada':dada,
               'uncle':uncle,
               }
    return render(request,"addname.html",context)