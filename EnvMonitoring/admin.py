from django.contrib import admin
from .models import ( Air , water ,
 Noise , TreeManagment , WasteTreatments , MaterialSourcing)

# Register your models here.
# admin.site.register(EnvMonitoring)
# admin.site.register(EnvQualityMonitoring)
admin.site.register(Air)
admin.site.register(water)
admin.site.register(Noise)
admin.site.register(TreeManagment)
admin.site.register(WasteTreatments)
admin.site.register(MaterialSourcing)
