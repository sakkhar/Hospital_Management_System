from django.contrib import admin
from .models import DoctorProfile

#class DoctorProfile(admin.ModelAdmin):
 #   list_display = ('first_name', 'last_name', 'email')
  #  list_filter = ('first_name', 'last_name', 'email')
   # search_fields = ('first_name', 'last_name', 'email')

# Register your models here.
admin.site.register(DoctorProfile)


