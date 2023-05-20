from django.contrib import admin

from .models import *


@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Analysis)
class AnalysisModelAdmin(admin.ModelAdmin):
    pass


@admin.register(New)
class NewModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(PatientInOrder)
class PatientInOrderModelAdmin(admin.ModelAdmin):
    pass


@admin.register(AnalysisInPatient)
class AnalysisInPatientModelAdmin(admin.ModelAdmin):
    pass
