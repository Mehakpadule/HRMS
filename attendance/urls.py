from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AttendanceViewSet,
    attendance_list_page,
    attendance_add_page,
    attendance_edit_page,
)


router = DefaultRouter()

router.register(
    'attendance',
    AttendanceViewSet,
    basename='attendance'
)


urlpatterns = [

    path(
        'attendance-list/',
        attendance_list_page,
        name='attendance-list'
    ),

    path(
        'attendance-add/',
        attendance_add_page,
        name='attendance-add'
    ),

    path(
        'attendance-edit/<int:pk>/',
        attendance_edit_page,
        name='attendance-edit'
    ),

] + router.urls