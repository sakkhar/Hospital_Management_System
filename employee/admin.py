from django.contrib import admin

# Register your models here.
from employee.models import Nurse, Laboratorist, Pharmacist


admin.site.register(Nurse)
admin.site.register(Laboratorist)
admin.site.register(Pharmacist)

