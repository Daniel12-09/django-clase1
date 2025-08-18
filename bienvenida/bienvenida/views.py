from django.http import HttpResponse
def inicio(request):
  nombre = "Daniel Conejeros"
  return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")