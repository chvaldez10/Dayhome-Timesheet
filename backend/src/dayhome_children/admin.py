from django.contrib import admin
from .models import DayHomeChildren

# Register your models here.
class DayHomeChildrenAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'first_name', 'last_name', 'provider_id')
    search_fields = ('first_name', 'last_name')

admin.site.register(DayHomeChildren, DayHomeChildrenAdmin)