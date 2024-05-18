from django.contrib import admin
from . models import Doctor, Department
from patient.models import Appointment


class DoctorAppointment(admin.TabularInline):
    model = Appointment


class DepartmentAppointment(admin.TabularInline):
    model = Appointment


admin.site.register(Department)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_name', Department, 'address', 'mobile', 'user']
    inlines = [DoctorAppointment, DepartmentAppointment]


admin.site.register(Doctor, DoctorAdmin)
