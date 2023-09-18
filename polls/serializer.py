from rest_framework import serializers
from .models import water, karta
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 


class waterSerializer(serializers.ModelSerializer):
    class Meta:
        model=water
        fields = ('name', 'date_of_invent', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(waterSerializer, self).create(validated_data)


class kartaSerializer(serializers.ModelSerializer):
    class Meta:
        model=karta
        fields=('comName', 'number', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(kartaSerializer, self).create(validated_data)



