import sys
from datetime import datetime

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import Adafruit_DHT

from models import SensorTemperatureHumidity
 
logger = get_task_logger(__name__)
import logging

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def test_task():
    logger.info("Start task")
    
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    sensorData = SensorTemperatureHumidity(
        temperature=temperature, 
        humidity=humidity
        )
    sensorData.save()

    logger.info("BOSTJAN NOVAK: Opravljeno")
