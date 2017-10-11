from django.contrib import admin
from patient.models import Admission, Appointment, MedicalTest

#from patient.models import Appointment

# Register your models here.
admin.site.register(Admission)
admin.site.register(Appointment)
admin.site.register(MedicalTest)
#admin.site.register(Statistics)
