from django.contrib import admin
from . models import Variable, SatModel, Sector, Unit

# Register your models here.
admin.site.register(Variable)
admin.site.register(SatModel)
admin.site.register(Sector)
admin.site.register(Unit)

