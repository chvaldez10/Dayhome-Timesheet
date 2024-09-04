from django.db import models
from core.models import TimeStampModel

class DayHomeChildren(TimeStampModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    provider_id = models.ForeignKey('dayhome_provider.DayHomeProvider', on_delete=models.CASCADE)

    class Meta:
        db_table = "dayhome_children"

    def __str__(self):
        return self.first_name + " " + self.last_name