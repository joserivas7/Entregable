from django.shortcuts import render
from django.http import HttpResponse
from Appclase.models import familia
from django.template import Template, Context




def familiares (request):

    fami=familia(nombre="Daniel", apellido="Rivas", parentesco="Hermano", edad=32)
    fami.save()
    fami={"nombre":fami.nombre, "apellido":fami.apellido, "parentesco":fami.parentesco, "edad":fami.edad}
 
    archivo=open("C:/Users/jose.rivas/Desktop/entorno2/Clase21/Plantillas/template.html")

    template=Template(archivo.read())
    archivo.close()
    contexto=Context(fami)
    documento=template.render(contexto)
    return HttpResponse (documento)