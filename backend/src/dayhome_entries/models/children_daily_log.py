from django.db import models
from core.models import TimeStampModel
from core.enum import DayhomeStatus

class ChildrenDailyLog(TimeStampModel):
    date_entry = models.DateField()
    sign_in_time = models.DateTimeField(null=True, blank=True)
    sign_out_time = models.DateTimeField(null=True, blank=True)
    total_time = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=DayhomeStatus.choices, default=DayhomeStatus.ABSENT)
    children_id = models.ForeignKey('dayhome_children.DayhomeChildren', on_delete=models.PROTECT)
    health_check = models.CharField(null=True, blank=True)
    
    class Meta:
        db_table = "dayhome_children_daily_log"

    def __str__(self):
        return f"{self.children.first_name} {self.children.last_name} - {self.date_entry}"
    