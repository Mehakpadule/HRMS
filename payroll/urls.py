from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    PayrollViewSet,
    payroll_list_page,
    payroll_add_page,
    payroll_edit_page,
)


router = DefaultRouter()

router.register(
    'payroll',
    PayrollViewSet,
    basename='payroll'
)


urlpatterns = [

    path(
        'payroll-list/',
        payroll_list_page,
        name='payroll-list'
    ),

    path(
        'payroll-add/',
        payroll_add_page,
        name='payroll-add'
    ),

    path(
        'payroll-edit/<int:pk>/',
        payroll_edit_page,
        name='payroll-edit'
    ),

] + router.urls