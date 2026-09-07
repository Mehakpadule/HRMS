

# Create your models here
from django.db import models
from employees.models import Employee


class Leave(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='leaves'
    )

    leave_type = models.CharField(
        max_length=50
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"
