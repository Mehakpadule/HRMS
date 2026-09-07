from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Attendance
from .serializers import AttendanceSerializer
from employees.permissions import IsAdminOrReadOnly


class AttendanceViewSet(viewsets.ModelViewSet):

    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]

    search_fields = [
        'employee__name',
        'status'
    ]

    filterset_fields = [
        'employee',
        'date',
        'status'
    ]

    ordering_fields = [
        'date',
        'status'
    ]


# ==============================
# Attendance Frontend Pages
# ==============================

def attendance_list_page(request):
    return render(
        request,
        'attendance/attendance_list.html'
    )


def attendance_add_page(request):
    return render(
        request,
        'attendance/attendance_add.html'
    )


def attendance_edit_page(request, pk):
    return render(
        request,
        'attendance/attendance_edit.html'
    )