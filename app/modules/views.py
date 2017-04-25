from rest_framework import viewsets
from models import SensorTemperatureHumidity
from serializers import SensorTemperatureHumiditySerializer

class SensorTemperatureHumidityViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing temperature and humidity from
        sensor
     """
    queryset = SensorTemperatureHumidity.objects.all()
    serializer_class = SensorTemperatureHumiditySerializer
