from django.db import models
from employees.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'date'],
                name='unique_employee_attendance'
            )
        ]

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"