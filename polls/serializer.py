from rest_framework import serializers
from .models import water, karta


class waterSerializer(serializers.ModelSerializer):
    class Meta:
        model=water
        fields = ('name', 'date_of_invent')


class kartaSerializer(serializers.ModelSerializer):
    class Meta:
        model=karta
        fields=('comName', 'number')



