from django.shortcuts import render, get_object_or_404
from .models import water, karta
from django.http import JsonResponse

# Create your views here.

def all(request):
    all=water.objects.all()
    mylist =[]
    for i in all:
        mylist.append({
            'name':i.name,
            'date_of_invent':i.date_of_invent
        })
    return JsonResponse(mylist, safe=False)
    


def detail(request, yourid):
    each = get_object_or_404(karta, id=yourid)
    data={'Company name':each.comName, 'Phone number':each.number}
    return JsonResponse(data, safe=False)