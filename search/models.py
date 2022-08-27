from django.db import models
from django.utils import timezone

# Create your models here.
class Sector(models.Model):

    sector_choice = (

        ('Water', 'Water'),
        ('Climate', 'Climate'),
        ('Energy', 'Energy'),
        ('Land', 'Land'),
        ('Socio-economic', 'Socio-economic'),
    )

    sector = models.CharField(max_length=400, choices = sector_choice, blank = True, null=True)

    def __str__(self):
        return self.sector


class Unit(models.Model):
    unit = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return self.unit


class Variable(models.Model):
    shortname = models.CharField(max_length=100)
    longname = models.CharField(max_length=400)
    description = models.TextField(blank = True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name="variable")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="variable", blank = True,  null=True)

    def __str__(self):
        return self.longname


class SatModel(models.Model):
    satellite_or_model_long = models.CharField(max_length=100, blank = True)
    satellite_or_model_short = models.CharField(max_length=400, blank = True)
    sensor = models.CharField(max_length=400, blank = True)
    product = models.CharField(max_length=400)
    variable = models.ForeignKey(Variable, on_delete=models.PROTECT, related_name="satmodel")
    start_date = models.DateField()
    end_date = models.DateField(default=timezone.now)
    reference = models.CharField(max_length=400, blank = True)

    def __str__(self):
        return self.satellite_or_model