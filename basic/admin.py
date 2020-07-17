from django.contrib import admin
from basic.models import *

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	"""Комнаты чата"""
	list_display = ("rank", "employer", "employees", "salary")


admin.site.register(Company, CompanyAdmin)
