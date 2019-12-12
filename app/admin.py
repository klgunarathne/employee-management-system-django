from django.contrib import admin

from app.models import Employee, Department, Allocation

admin.site.site_header = "Employe Management System"
@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ('employee_name', 'status')
    list_filter = ['status']
    search_fields = ['status', 'employee_name']


@admin.register(Department)
class EmployeeModel(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name',]
    search_fields = ['name', ]


@admin.register(Allocation)
class EmployeeModel(admin.ModelAdmin):
    list_display = ('employee_no', 'department_no', 'working_hours')
    list_filter = ['employee_no']
    search_fields = ['employee_no', 'department_no']

