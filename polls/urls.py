from django.urls import path

from .views import GetAllWater, PostWater, GetDetailWater, PatchWater, DeleteWater, AllFunctionWater, PostGetWater


from .views import GetAllKarta, GetDetailKarta, PostKarta, PatchKarta, DeleteKarta, AllFunctionKarta, PostGetKarta

urlpatterns=[
        path('GetAllKarta/', GetAllKarta.as_view()),
    path('GetDetailKarta/<int:pk>', GetDetailKarta.as_view()),
    path('PostKarta/', PostKarta.as_view() ),
    path('PatchKarta/<int:pk>', PatchKarta.as_view()),
    path('DeleteKarta/<int:pk>', DeleteKarta.as_view()),
    path('PostGetKarta/', PostGetKarta.as_view()),
    path('AllFunctionKarta/<int:pk>', AllFunctionKarta.as_view())
    ,
    path('GetAllWater/', GetAllWater.as_view()),
    path('GetDetailWater/<int:pk>', GetDetailWater.as_view()),
    path('PostWater/', PostWater.as_view() ),
    path('PatchWater/<int:pk>', PatchWater.as_view()),
    path('DeleteWater/<int:pk>', DeleteWater.as_view()),
    path('PostGetWater/', PostGetWater.as_view()),
    path('AllFunctionWater/<int:pk>', AllFunctionWater.as_view())



]