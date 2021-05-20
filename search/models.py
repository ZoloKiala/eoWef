from django.db import models
from django.utils import timezone

# Create your models here.

class Variables(models.Model):
    shortname = models.CharField(max_length=100)
    longname = models.CharField(max_length=400)
    description = models.TextField(blank = True, null=True)
    
    def __str__(self):
        return self.longname

class SatModel(models.Model):

    
    sector_choice = (
        
            ('Water', 'Water'),
            ('Climate', 'Climate'),
            ('Energy', 'Energy'),
            ('Land', 'Land'),
            ('Socio-economic', 'Socio-economic'),

        )
    variable = models.ForeignKey(Variables, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100, blank = True)
    shortname = models.CharField(max_length=100)
    longname = models.CharField(max_length=400)
    sensor = models.CharField(max_length=400, blank = True)
    product = models.CharField(max_length=400)
    description = models.TextField(blank = True)
    start_date = models.DateField()
    end_date = models.DateField(default=timezone.now)
    sector = models.CharField(max_length=400, choices = sector_choice, null=False)
    reference = models.URLField(max_length=400)

    def __str__(self):
        return self.shortname