from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0003_alter_department_id_alter_employee_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="department_old",
            field=models.CharField(
                max_length=100,
                null=True,
                blank=True
            ),
        ),
    ]