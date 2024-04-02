from django.http import HttpResponse
from django.template import Template, Context

def saludar(request):
    return HttpResponse("<h1>¡Hola! Bienvenido a mi aplicación.</h1>")

def segunda_vista(request):
    return HttpResponse("<br><br> no seas trolo eze :)")
def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"

    return HttpResponse (documentoDeTexto)

import os

def probandoTemplate(request):
    # Obtener la ruta del archivo template1.html
    template_path = os.path.join(os.path.dirname(__file__), 'platillas', 'template1.html')
    # Abrir el archivo usando un contexto de lectura para garantizar su cierre adecuado
    with open(template_path, 'r') as template_file:
        # Leer el contenido del archivo
        template_content = template_file.read()

    # Crear el objeto Template
    plantilla = Template(template_content)

    # Renderizar la plantilla con un contexto vacío
    documento = plantilla.render(Context())

    # Retornar la respuesta HTTP con el contenido renderizado
    return HttpResponse(documento)
