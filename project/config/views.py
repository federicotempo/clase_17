from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola django - Coder")

def segunda_vista(request):
    return HttpResponse("<h1>Segunda vista<h1>")