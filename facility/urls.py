from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Endpoints that allows date range filtering, for generating charts
router.register(r'hospital-admission', views.TotalHospitalAdmissionRangeViewSet)
router.register(r'icu-admission', views.TotalICUAdmissionRangeViewSet)
router.register(r'pkrc-admission', views.TotalPKRCAdmissionRangeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
