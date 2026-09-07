from rest_framework import serializers
from datetime import date
from .models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'

    def validate_status(self, value):

        if value not in ['Present', 'Absent', 'Leave']:
            raise serializers.ValidationError(
                "Status must be Present, Absent or Leave."
            )

        return value

    def validate_date(self, value):

        if value > date.today():
            raise serializers.ValidationError(
                "Attendance date cannot be in the future."
            )

        return value