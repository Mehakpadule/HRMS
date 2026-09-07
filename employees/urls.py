from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeViewSet,
    DepartmentViewSet,
    login_page,
    dashboard_page,
    employee_list_page,
    employee_add_page,
    employee_edit_page,
    department_list_page,
    department_add_page,

    department_edit_page,
)

router = DefaultRouter()

router.register(
    'employees',
    EmployeeViewSet,
    basename='employee'
)

router.register(
    'departments',
    DepartmentViewSet,
    basename='department'
)

urlpatterns = [

    # Login
    path(
        'login/',
        login_page,
        name='login'
    ),

    # Dashboard
    path(
        'dashboard/',
        dashboard_page,
        name='dashboard'
    ),

    # Employee List
    path(
        'employee-list/',
        employee_list_page,
        name='employee-list'
    ),

    # Add Employee
    path(
        'employee-add/',
        employee_add_page,
        name='employee-add'
    ),

    # Edit Employee
    path(
        'employee-edit/<int:pk>/',
        employee_edit_page,
        name='employee-edit'
    ),

    # Department List
    path(
        'department-list/',
        department_list_page,
        name='department-list'

    ),
    path(
    'department-add/',
    department_add_page,
    name='department-add'
),

path(
    'department-edit/<int:pk>/',
    department_edit_page,
    name='department-edit'
),

] + router.urls