from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vizualisation, Edge, Node


def index(request):
    template = loader.get_template('vizualisations/index.html')
    vizualisation_list = Vizualisation.objects.all()
    context = {
        'vizualisation_list': vizualisation_list,
    }
    return HttpResponse(template.render(context, request))

def view(request, vizualisation_id):
    template = loader.get_template('vizualisations/view.html')
    edge_list = Edge.objects.filter(vizualisation=vizualisation_id)
    vizualisation = Vizualisation.objects.get(pk=vizualisation_id)
    node_list = []
    edges=Edge.objects.filter(vizualisation=vizualisation_id)
    for edge in edges:
        node_list.append(edge.src)
        node_list.append(edge.dest)
    node_list=set(node_list)
    context = {
        'node_list': node_list,
        'edge_list': edge_list,
        'vizualisation': vizualisation
    }
    return HttpResponse(template.render(context, request))