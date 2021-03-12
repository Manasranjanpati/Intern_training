from django.contrib import admin
from .models import Company, Employee


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','email','contact_number','desription']
    list_filter = ['name','email']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_name','employee_phone','employee_adress','employee_id','employee_company']
    list_filter = ['employee_name', 'employee_id']