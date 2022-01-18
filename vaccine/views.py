from rest_framework import viewsets, views
from rest_framework import permissions
from .models import Vaccination
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class TotalCompletedVaccinationRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Vaccination.objects.all().order_by('date')
    serializer_class = TotalCompletedVaccinationRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }
