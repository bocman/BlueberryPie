from django.db import models
from django.utils import timezone

class SensorTemperatureHumidity(models.Model):
    """
    Class is used to store temperature and humidity data from
    sensor
    """
    class Meta:
        db_table = 'data_temperature_humidity'

    temperature = models.PositiveIntegerField(
        default=None, null=True
        )

    humidity = models.PositiveSmallIntegerField(
        default=None, null=True
        )
    gpio_id = models.PositiveIntegerField(
        default=None, null=True
    ) 

    timestamp = models.DateTimeField(
        editable=False
    )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.timestamp = timezone.now()
        return super(SensorTemperatureHumidity, self).save(*args, **kwargs)
