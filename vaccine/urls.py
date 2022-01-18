from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'completed-vaccination', views.TotalCompletedVaccinationRangeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
