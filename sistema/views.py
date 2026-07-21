from django.http import HttpResponse

def hola(request):
    return HttpResponse("<h1>¡Proyecto Django funcionando exitosamente!</h1><p>Esta es la prueba de la modificación.</p>")