from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Endpoints that allows date range filtering, for generating charts
router.register(r'hospital-admission', views.TotalHospitalAdmissionRangeSerializer)
router.register(r'icu-admission', views.TotalICUAdmissionRangeSerializer)
router.register(r'pkrc-admission', views.TotalPKRCAdmissionRangeSerializer)

urlpatterns = [
    path('', include(router.urls)),
]
