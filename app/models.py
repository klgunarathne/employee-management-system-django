from django.db import models


class Employee(models.Model):
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('TEMPORARY', 'TEMPORARY')
    )
    employee_name = models.CharField(blank=False, max_length=100)
    status = models.CharField(blank=True, max_length=10, choices=STATUS)

    def __str__(self):
        return self.employee_name


class Department(models.Model):
    name = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name


class Allocation(models.Model):
    employee_no = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_no = models.ForeignKey(Department, on_delete=models.CASCADE)
    working_hours = models.DecimalField(default=0.0, blank=True, decimal_places=2, max_digits=5)

