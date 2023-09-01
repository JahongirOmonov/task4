from django.shortcuts import render, get_object_or_404
from .models import water, karta
from django.http import JsonResponse
from .serializer import waterSerializer, kartaSerializer

# Create your views here.

def all(request):
    all=water.objects.all()
    result=waterSerializer(all, many=True)
    # for i in all:
    #     mylist.append({
    #         'name':i.name,
    #         'date_of_invent':i.date_of_invent
    #     })
    return JsonResponse(result.data, safe=False)
    


def detail(request, yourid):
    some = karta.objects.filter(id=myid)
    forgett = kartaSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)