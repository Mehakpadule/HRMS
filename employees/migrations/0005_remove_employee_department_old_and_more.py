from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_add_department_old'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(
                    model_name='employee',
                    name='department_old',
                ),
                migrations.AlterField(
                    model_name='employee',
                    name='department',
                    field=models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='employees.department',
                    ),
                ),
            ],
        ),
    ]