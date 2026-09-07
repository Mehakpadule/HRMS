from rest_framework import serializers
from .models import Leave


class LeaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Leave
        fields = '__all__'

    def validate(self, data):

        start_date = data.get('start_date')
        end_date = data.get('end_date')
        status = data.get('status')

        if start_date and end_date and end_date < start_date:
            raise serializers.ValidationError(
                "End date cannot be before start date."
            )

        if status not in ['Pending', 'Approved', 'Rejected']:
            raise serializers.ValidationError(
                "Invalid status. Use Pending, Approved or Rejected."
            )

        return data