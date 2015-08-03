from django.shortcuts import render
from django.contrib.auth.models import User, Group
from client.serializers import UserSerializer, GroupSerializer, GPIOSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from models import device_GPIO

import webAPI.settings as settings

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
        item_id = kwargs.get('pk', None)
        if 'is_activated' in request.data:
            status = request.data.get('is_activated', None)
            if settings.CLIENT_TYPE == "raspberry":
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, status)

         
            print "sem ja"
        else:
            print "nisem ne"

        return self.update(request, *args, **kwargs)
        