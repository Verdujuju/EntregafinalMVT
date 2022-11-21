from django.shortcuts import render
from django.http import HttpResponse
from AppFlia.models import Familia
from django.template import loader

def flia_db(request):
    mimujer = Familia(nombre = "Ale Regla", fecha_nacim = 1981-12-16, dni = 28888888)
    mihija = Familia(nombre = "Lara Rosenman", fecha_nacim = 2016-9-2, dni = 55888888)
    mihermana = Familia(nombre = "Maria Sol Rosenman", fecha_nacim = 1983-3-20, dni = 31111111)

    mimujer.save()
    mihija.save()
    mihermana.save()

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
    plantilla = loader.get_template("template_1.html")
    doc = plantilla.render(dic)

    return HttpResponse(doc)





