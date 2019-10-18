from django.http import HttpResponse

from django.template import loader

from encuestas.models import Pregunta


def index(request):
    listado = Pregunta.objects.order_by('-fecha_publicacion')[:10]
    template = loader.get_template('encuestas/index.html')
    context = {
        'listado': listado,
    }
    return HttpResponse(template.render(context, request))

def detalle(request, pregunta_id):
    pregunta = Pregunta.objects.get(id=pregunta_id)
    template = loader.get_template('encuestas/detalle.html')
    context = {
        'pregunta': pregunta,
    }
    return HttpResponse(template.render(context, request))


def resultados(request, total):
	latest_question_list = Pregunta.objects.order_by('-fecha_publicacion')[:total]
	output = ', '.join([q.descripcion for q in latest_question_list])
	return HttpResponse(output)

"""
	Construya una vista que retorne todas las opciones de una pregunta específica.
	*Filtrar por ID de Pregunta
"""