from django.db import models
from core.models import TimeStampModel

class DayhomeProvider(TimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = "dayhome_provider"

    def __str__(self):
        return self.first_name + " " + self.last_name
