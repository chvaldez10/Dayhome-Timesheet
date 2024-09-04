from django.contrib import admin
from .models import DayHomeProvider

class DayHomeProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'location', 'email')
    search_fields = ('first_name', 'last_name', 'location')

admin.site.register(DayHomeProvider, DayHomeProviderAdmin)