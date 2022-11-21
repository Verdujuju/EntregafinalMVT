from django.shortcuts import render
from django.http import HttpResponse
from AppFlia.models import Familia
from django.template import loader
#Importo render, HttpResonse, clase familia y loader para el HTML

def flia_db(request): #Datos que completan la BD (de la clase Familia)
    mimujer = Familia(nombre = "Ale Regla", fecha_nacim ="1980-12-16", dni = 28888888)
    mihija = Familia(nombre = "Lara Rosenman", fecha_nacim = "2016-09-02", dni = 55888888)
    mihermana = Familia(nombre = "Maria Sol Rosenman", fecha_nacim = "1983-03-20", dni = 31111111)

    mimujer.save()
    mihija.save()
    mihermana.save()   
    #Guardo los cambios en variables

    

    dic = {
        "nombre_mimujer": mimujer.nombre,
        "fechanacim_mimujer": mimujer.fecha_nacim,
        "dni_mimujer": mimujer.dni,
        "nombre_mihija": mihija.nombre,
        "fechanacim_mihija": mihija.fecha_nacim,
        "dni_mihija": mihija.dni,        
        "nombre_mihermana": mihermana.nombre,
        "fechanacim_mihermana": mihermana.fecha_nacim,
        "dni_mihermana": mihermana.dni
        }
    #Diccionario del cual se van a sacar los datos para el HTML (Voy a usar la clave siempre)
    
    plantilla = loader.get_template("template1.html") #Llamo al template (Ojo con el nombre)
    doc = plantilla.render(dic)

    return HttpResponse(doc) #Documento que va a devolver
    





