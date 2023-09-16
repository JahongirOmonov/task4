from django.shortcuts import render, get_object_or_404
from .models import water, karta
from django.http import JsonResponse
from .serializer import waterSerializer, kartaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

# Create your views here.

# def all(request):
#     all=water.objects.all()
#     result=waterSerializer(all, many=True)
#     # for i in all:
#     #     mylist.append({
#     #         'name':i.name,
#     #         'date_of_invent':i.date_of_invent
#     #     })
#     return JsonResponse(result.data, safe=False)

# class getwater(APIView):
#     def get(self, request):
#         kalla = water.objects.all()
#         barakalla=waterSerializer(kalla, many=True)
#         return Response(barakalla.data)
class GetAllWater(generics.ListAPIView):
    queryset=water.objects.all()
    serializer_class=waterSerializer




class GetDetailWater(generics.RetrieveAPIView):
    queryset = water.objects.all()

    serializer_class=waterSerializer

class PostWater(generics.CreateAPIView):



    queryset=water.objects.all()
    serializer_class=waterSerializer

class PatchWater(generics.UpdateAPIView):
    queryset=water.objects.all()
    serializer_class=waterSerializer





# def detail(request, yourid):
#     some = karta.objects.filter(id=myid)
#     forgett = kartaSerializer(some, many=True)
#     return JsonResponse(forgett.data, safe=False)



class DeleteWater(generics.DestroyAPIView):
    queryset=water.objects.all()
    serializer_class=waterSerializer

class PostGetWater(generics.ListCreateAPIView):
    queryset=water.objects.all()
    serializer_class=waterSerializer

class AllFunctionWater(generics.RetrieveUpdateDestroyAPIView):
    queryset=water.objects.all()
    serializer_class=waterSerializer


    


# def detail(request, yourid):
#     some = karta.objects.filter(id=myid)
#     forgett = kartaSerializer(some, many=True)
#     return JsonResponse(forgett.data, safe=False)

# class postwater(APIView):
#     def post(self, request):
#         main_body=request.data
#         sss = waterSerializer(data=main_body)
#         if sss.is_valid():
#             sss.save()
#             return Response(sss.data)
#         return Response(sss.errors)


class GetAllKarta(generics.ListAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer

class GetDetailKarta(generics.RetrieveAPIView):
    queryset = karta.objects.all()
    serializer_class=kartaSerializer


class AllFunctionKarta(generics.RetrieveUpdateDestroyAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer

class PostKarta(generics.CreateAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer
# class postwater(APIView):
#     def post(self, request):
#         main_body=request.data
#         sss = waterSerializer(data=main_body)
#         if sss.is_valid():
#             sss.save()
#             return Response(sss.data)
#         return Response(sss.errors)

class PatchKarta(generics.UpdateAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer

class DeleteKarta(generics.DestroyAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer



class PostGetKarta(generics.ListCreateAPIView):
    queryset=karta.objects.all()
    serializer_class=kartaSerializer


