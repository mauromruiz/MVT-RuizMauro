
from django.http import HttpResponse
from django.template import Context, Template

def pagina1(request):
    return HttpResponse('<h1> Primera Pagina</h1>')

def mi_template(request):

    cargar_archivo = open(r'C:\Proyectos Python\MVT+RuizMauro\Templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()

    contexto = Context()

    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)