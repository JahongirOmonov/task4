from django.urls import path
from .views import getwater, postwater, detail

urlpatterns=[
    path('all/', getwater.as_view()),
    path('detail/<int:yourid>', detail),
    path('create/', postwater)
]