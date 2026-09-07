from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Leave
from .serializers import LeaveSerializer
from employees.permissions import IsAdminOrReadOnly


class LeaveViewSet(viewsets.ModelViewSet):

    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]

    search_fields = [
        'leave_type',
        'reason',
        'status'
    ]

    filterset_fields = [
        'employee',
        'leave_type',
        'status'
    ]

    ordering_fields = [
        'start_date',
        'end_date',
        'created_at'
    ]


# =========================
# LEAVE FRONTEND PAGES
# =========================

def leave_list_page(request):

    return render(
        request,
        'leaves/leave_list.html'
    )


def leave_add_page(request):

    return render(
        request,
        'leaves/leave_add.html'
    )


def leave_edit_page(request, pk):

    return render(
        request,
        'leaves/leave_edit.html'
    )