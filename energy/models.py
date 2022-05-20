from django.db import models


class Company(models.Model):

    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"


class Meter(models.Model):

    class MeterType(models.TextChoices):
        CONSUMPTION = 'consumption'
        GENERATION = 'generation'

    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    meter_type = models.CharField(max_length=20, choices=MeterType.choices)
    meter_name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.company} - {self.meter_name}"


class Measurement(models.Model):

    meter = models.ForeignKey('Meter', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    voltage = models.FloatField()
    current = models.FloatField()
    active_power = models.FloatField()
    reactive_power = models.FloatField()
