from django.contrib import admin

# Register your models here.
from monitor_hospital.models import Payment_History, Bed_Allotment, Blood_Bank, Blood_Donor, Medicine, Operation_Report, birth_report, death_report

admin.site.register(Payment_History)
admin.site.register(Bed_Allotment)
admin.site.register(Blood_Donor)
admin.site.register(Blood_Bank)
admin.site.register(Medicine)
admin.site.register(Operation_Report)
admin.site.register(birth_report)
admin.site.register(death_report)
