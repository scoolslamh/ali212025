from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['title', 'generated_on']
    search_fields = ['title']
    list_filter = ['generated_on']
