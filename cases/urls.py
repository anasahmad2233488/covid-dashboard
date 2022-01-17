from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Endpoints for summary of statistics on specific date
router.register(r'cases-summary', views.DailyCasesViewSet)
router.register(r'tests-summary', views.DailyTestsViewSet)
router.register(r'checkin-summary', views.DailyCheckinsViewSet)

# Endpoints for aggregated statistics on specific date ranges
#router.register(r'cases-summary-period', views.CasesPeriodSummaryView.as_view(), basename='cases-period-summary')
#router.register(r'cluster-summary-period', views.ClusterPeriodSummaryViewSet, basename='cases-period-summary')
#router.register(r'tests-summary-period', views.TestsPeriodSummaryViewSet, basename='cases-period-summary')
#router.register(r'checkin-summary-period', views.CheckinsPeriodSummaryViewSet, basename='cases-period-summary')

# Endpoints that allows date range filtering, for generating charts
router.register(r'daily-new-cases', views.NewCasesRangeViewSet)
router.register(r'total-cases', views.TotalCasesRangeViewSet)
router.register(r'death', views.DeathRangeViewSet)
router.register(r'recovery', views.RecoveryRangeViewSet)
router.register(r'checkins', views.CheckinsRangeViewSet)
router.register(r'individual-checkins', views.IndCheckinsRangeViewSet)
router.register(r'checkin-locations', views.CheckinLocationsRangeViewSet)

urlpatterns = [
    path(r'cases-summary-period/', views.CasesPeriodSummaryView.as_view(), name='cases-period-summary'),
    path(r'cluster-summary-period/', views.ClusterPeriodSummaryView.as_view(), name='cases-period-summary'),
    path(r'tests-summary-period/', views.TestsPeriodSummaryView.as_view(), name='cases-period-summary'),
    path(r'checkin-summary-period/', views.CheckinsPeriodSummaryView.as_view(), name='cases-period-summary'),
    path('', include(router.urls)),
]
