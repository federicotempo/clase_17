#Esto es el controlador
from django.http import HttpResponse
from django.shortcuts import render
# from django.template import Context, Template
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola django - Coder")

def segunda_vista(request):
    return HttpResponse("<h1>Segunda vista<h1>")

def nombre(request, nombre, apellido):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
    # mi_html = open("./templates/template1.html")
    # mi_template = Template(mi_html.read())
    # mi_html.close()
    nombre = "Louis" #! NUEVO
    apellido = "Van Beethoven" #! NUEVO
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f") #! NUEVO
    datos = {"nombre": nombre, "apellido": apellido, "fecha": ahora} #! NUEVO
    # mi_contexto = Context(datos) #! cambio
    # mi_documento = mi_template.render(mi_contexto)
    # return HttpResponse(mi_documento)
    return render(request, "template1.html", datos)

def fecha_hora(request):
    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:S.%f")
    return HttpResponse(f"<h1>Fecha y hora: {ahora} </h1>")

def mis_notas(request):
    lista_de_notas = [2, 3, 5, 7, 9, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "notas.html", contexto)

def nuevo_template(request):
    parciales = [10, 10, 10]
    contexto = {"parciales": parciales}
    return render(request, "nuevo_template.ht", contexto)

def diccionario(request):
    mi_diccionario = {"persona": {"nombre" : "Cintia", "edad": 38}}
    return render(request, "prueba.html", mi_diccionario)