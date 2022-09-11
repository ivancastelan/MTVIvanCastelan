from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from MTVApp.models import *

def familiar1(request):

    familiar = Familiar(name="Marisol Aguilar", age=51)
    birthd = Fecha("1970-09-15")
    diccionario = {"name":familiar.name, "age":familiar.age, "cumpleanos":birthd}
    plantilla = loader.get_template("familiar1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def familiar2(request):

    familiar = Familiar(name="Diana Castelan", age=27)
    birthd = Fecha("1995-09-05")
    diccionario = {"name":familiar.name, "age":familiar.age, "cumpleanos":birthd}
    plantilla = loader.get_template("familiar2.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def familiar3(request):

    familiar = Familiar(name="Aarón Aguilar", age=17)
    birthd = Fecha("2005-04-15")
    diccionario = {"name":familiar.name, "age":familiar.age, "cumpleanos":birthd}
    plantilla = loader.get_template("familiar3.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

