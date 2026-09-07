from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    LeaveViewSet,
    leave_list_page,
    leave_add_page,
    leave_edit_page,
)


router = DefaultRouter()

router.register(
    'leaves',
    LeaveViewSet,
    basename='leave'
)


urlpatterns = [

    path(
        'leave-list/',
        leave_list_page,
        name='leave-list'
    ),

    path(
        'leave-add/',
        leave_add_page,
        name='leave-add'
    ),

    path(
        'leave-edit/<int:pk>/',
        leave_edit_page,
        name='leave-edit'
    ),

] + router.urls