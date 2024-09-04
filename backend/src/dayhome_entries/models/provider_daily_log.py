from django.db import models
from core.models import TimeStampModel

class ProviderDailyLog(TimeStampModel):
    date_entry = models.DateField()
    sign_in_time = models.DateTimeField(null=True, blank=True)
    sign_out_time = models.DateTimeField(null=True, blank=True)
    total_time = models.FloatField(default=0)
    provider_id = models.ForeignKey('dayhome_provider.DayhomeProvider', on_delete=models.PROTECT)
    
    class Meta:
        db_table = "dayhome_provider_daily_log"

    def __str__(self):
        return f"{self.provider_id.first_name} {self.provider_id.last_name} - {self.date_entry}"