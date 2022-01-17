from rest_framework import viewsets, views
from rest_framework import permissions
from .models import ICU, PKRC, Hospital
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class TotalHospitalAdmissionRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Hospital.objects.all().order_by('date')
    serializer_class = TotalHospitalAdmissionRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }



class TotalICUAdmissionRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = ICU.objects.all().order_by('date')
    serializer_class = TotalICUAdmissionRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class TotalPKRCAdmissionRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = PKRC.objects.all().order_by('date')
    serializer_class = TotalPKRCAdmissionRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }
