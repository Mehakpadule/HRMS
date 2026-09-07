from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Payroll
from .serializers import PayrollSerializer
from employees.permissions import IsAdminOrReadOnly


class PayrollViewSet(viewsets.ModelViewSet):

    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]

    search_fields = [
        'month',
        'payment_status',
        'employee__name'
    ]

    filterset_fields = [
        'employee',
        'month',
        'payment_status'
    ]

    ordering_fields = [
        'month',
        'net_salary',
        'created_at'
    ]


# =========================
# PAYROLL FRONTEND PAGES
# =========================

def payroll_list_page(request):
    return render(
        request,
        'payroll/payroll_list.html'
    )


def payroll_add_page(request):
    return render(
        request,
        'payroll/payroll_add.html'
    )


def payroll_edit_page(request, pk):
    return render(
        request,
        'payroll/payroll_edit.html'
    )