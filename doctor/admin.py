from django.contrib import admin
#from doctor.models import
#class DoctorProfile(admin.ModelAdmin):
 #   list_display = ('first_name', 'last_name', 'email')
  #  list_filter = ('first_name', 'last_name', 'email')
   # search_fields = ('first_name', 'last_name', 'email')

# Register your models here.
from doctor.models import DoctorProfile, Nurse, Administrator

admin.site.register(DoctorProfile)
admin.site.register(Nurse)
admin.site.register(Administrator)




