from django.shortcuts import render
from django.contrib.auth.models import User, Group
from client.serializers import UserSerializer, GroupSerializer, GPIOSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import time

import requests

from models import device_GPIO
import webAPI.settings as settings


if settings.CLIENT_TYPE == "raspberry":
    import RPi.GPIO as GPIO
    import pigpio

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GPIOListView(generics.ListAPIView):
    queryset = device_GPIO.objects.all()
    serializer_class = GPIOSerializer

class GPIODetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    TODO
    """
    queryset = device_GPIO.objects.all()
    serializer_class = GPIOSerializer

    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        item_id = int(kwargs.get('pk', None))
        if 'is_activated' in request.data:
            status = request.data.get('is_activated', None)
            status = False if status == 'True' else True
            print "----------"
            print status 
            print "----------"
            if settings.CLIENT_TYPE == "raspberry":
                #GPIO.setmode(GPIO.BOARD)
                #GPIO.setup(item_id, GPIO.OUT)
                #GPIO.output(item_id, status)
                pi = pigpio.pi()
                pi.write(item_id, status)
        return self.update(request, *args, **kwargs)


class Ping(APIView):
    """
    This method is called by server side to check if this
    client is connected. It's simple ping method which return
    response 200, if everything is ok.
    """
    def get(self, request, *args, **kwargs):
        return Response(status=requests.codes.ok) 
