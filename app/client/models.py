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

    humidity = models.PositiveIntegerField(
        default=None, null=True
        )

    timestamp = models.DateTimeField(
        editable=False
    )

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.timestamp = timezone.now()
        return super(SensorTemperatureHumidity, self).save(*args, **kwargs)



class device_GPIO(models.Model):

    """
    Class is used to hold information about some specific item. Item can 
    be related with client or not (Example: Webservice, which get data from web).
    Item can be defined as object, which get info(Service, sensors on GPIO ...) or
    can show result on the output.
    """
    class Meta:
        db_table = 'GPIO'

    name = models.CharField(
        max_length=30,
        default ="Not set yet"
    )
    description = models.CharField(
        max_length=30,
        default ="Not set yet"
    )
    is_general = models.BooleanField(
        default=False,
        blank=False, null=False
        )
    pin_number = models.PositiveIntegerField(
        default=None, null=True
        )
    interval = models.PositiveIntegerField(
        default=0, null=True,
        blank=False,
        verbose_name="Time interval",
        )
    is_input = models.NullBooleanField(
        default=False,
        blank=True, null=True
        )
    client = models.PositiveIntegerField(
        default=None
        )
#    group = models.PositiveIntegerField(
 #       default=None,
  #      )
    is_deleted = models.BooleanField(
        default=False,
    )
    is_activated = models.BooleanField(
        default=False,
        null=False, blank=False,
    )
    is_used = models.BooleanField(
        default=False,
        blank=False, null=False
        )

    def __str__(self):
        pass
    
