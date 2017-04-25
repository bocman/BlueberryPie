from rest_framework import serializers

from models import SensorTemperatureHumidity

class SensorTemperatureHumiditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SensorTemperatureHumidity
        fields = ('temperature', 'humidity', 'gpio_pin', 'timestamp')

    temperature = serializers.IntegerField()
    humidity = serializers.IntegerField()
    gpio_pin = serializers.IntegerField()
    timestamp = serializers.DateTimeField()

    