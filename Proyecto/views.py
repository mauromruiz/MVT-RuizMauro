
from django.http import HttpResponse

def pagina1(request):
    return HttpResponse('<h1> Primera Pagina</h1>')