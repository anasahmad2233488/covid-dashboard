from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path(r'cases/', views.predictCasesView.as_view(), name='predict-cases'),
    path('', include(router.urls)),
]
