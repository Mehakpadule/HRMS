

# Create your models here.
from django.db import models
from employees.models import Employee


class Payroll(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='payrolls'
    )

    month = models.CharField(
        max_length=20
    )

    basic_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    allowances = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    deductions = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    net_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.name} - {self.month}"