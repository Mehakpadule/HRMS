from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Employee, Department
from .serializers import EmployeeSerializer, DepartmentSerializer
from .permissions import IsAdminOrReadOnly


class EmployeeViewSet(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminOrReadOnly]

    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter
    ]

    search_fields = [
        'name',
        'email',
        'department',
        'designation'
    ]

    filterset_fields = [
        'department',
        'designation'
    ]

    ordering_fields = [
        'salary',
        'joining_date',
        'name'
    ]


class DepartmentViewSet(viewsets.ModelViewSet):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


def login_page(request):
    return render(request, 'login.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')


def employee_list_page(request):
    return render(request, 'employees/employee_list.html')

def employee_add_page(request):
    return render(request, 'employees/employee_add.html')

def employee_edit_page(request, pk):
    return render(request, 'employees/employee_edit.html')

def department_list_page(request):
    return render(request, 'departments/department_list.html')

def department_add_page(request):
    return render(
        request,
        'departments/department_add.html'
    )


def department_edit_page(request, pk):
    return render(
        request,
        'departments/department_edit.html'
    )