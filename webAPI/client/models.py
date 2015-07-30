from django.db import models


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
    group = models.PositiveIntegerField(
        default=None,
        )
    is_deleted = models.BooleanField(
        default=False,
    )
    is_activated = models.BooleanField(
        default=False,
        null=False, blank=False,
    )

    def __str__(self):
        pass
    
