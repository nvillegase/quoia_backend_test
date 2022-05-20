from django.contrib import admin
from energy import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(models.Meter)
class MeterAdmin(admin.ModelAdmin):
    list_display = ['company', 'meter_type', 'meter_name']


@admin.register(models.Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = [
        'meter',
        'date_time',
        'voltage',
        'current',
        'active_power',
        'reactive_power',
    ]
