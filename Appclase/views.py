from django.shortcuts import render
from django.http import HttpResponse
from Appclase.models import familia
from django.template import Template, Context
from django.template import loader



def familiares (request):

    fami=familia(nombre="Daniel", apellido="Rivas", parentesco="Hermano", edad=32)
    fami.save()
    fami={"nombre":fami.nombre, "apellido":fami.apellido, "parentesco":fami.parentesco, "edad":fami.edad}
 
    template=loader.get_template("template.html")

    documento=template.render(fami)
    return HttpResponse (documento)

