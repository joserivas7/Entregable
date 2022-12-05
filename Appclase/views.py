from django.shortcuts import render
from django.http import HttpResponse
from Appclase.models import familia
from django.template import Template, Context
from django.template import loader



def familiares (request):

    fami=familia(nombre="Daniel", apellido="Rivas", parentesco="Hermano", edad=22, fecha_nacimineto="1992-10-13")
    fami2=familia(nombre="Jose", apellido="Rivas", parentesco="Primo", edad=32, fecha_nacimineto="1985-10-13")
    fami3=familia(nombre="David", apellido="Rivas", parentesco="Tio", edad=42, fecha_nacimineto="1975-10-13")
    fami.save()
    fami2.save()
    fami3.save()

    fami={"nombre":fami.nombre, "apellido":fami.apellido, "parentesco":fami.parentesco, "edad":fami.edad, "fecha_nacimineto":fami.fecha_nacimineto,
    "nombre2":fami2.nombre, "apellido2":fami2.apellido, "parentesco2":fami2.parentesco, "edad2":fami2.edad,"fecha_nacimineto2":fami2.fecha_nacimineto,
    "nombre3":fami3.nombre, "apellido3":fami3.apellido, "parentesco3":fami3.parentesco, "edad3":fami3.edad, "fecha_nacimineto3":fami3.fecha_nacimineto
    }
 
    template=loader.get_template("template.html")

    documento=template.render(fami)
    return HttpResponse (documento)

