from rest_framework import serializers

from .models import Payroll


class PayrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payroll
        fields = '__all__'

    def validate(self, data):

        basic_salary = data.get('basic_salary', 0)
        allowances = data.get('allowances', 0)
        deductions = data.get('deductions', 0)

        if basic_salary < 0:
            raise serializers.ValidationError(
                "Basic salary cannot be negative."
            )

        if allowances < 0:
            raise serializers.ValidationError(
                "Allowances cannot be negative."
            )

        if deductions < 0:
            raise serializers.ValidationError(
                "Deductions cannot be negative."
            )

        if deductions > basic_salary + allowances:
            raise serializers.ValidationError(
                "Deductions cannot be greater than total salary."
            )

        data['net_salary'] = (
            basic_salary +
            allowances -
            deductions
        )

        return data