from rest_framework import viewsets, views
from rest_framework import permissions
from .models import Cases, MySJ, Tests
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum


class DailyCasesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Cases.objects.all().order_by('date')
    serializer_class = DailyCasesSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact']
    }

class DailyTestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Tests.objects.all().order_by('date')
    serializer_class = DailyTestsSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact']
    }

class DailyCheckinsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = MySJ.objects.all().order_by('date')
    serializer_class = DailyCheckinsSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact']
    }

class CasesPeriodSummaryView(views.APIView):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        state = request.query_params['state']
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']

        obj = Cases.objects.filter(state=state, date__gte=start_date, date__lte=end_date)
        count = obj.count()
        sum_new_cases = obj.aggregate(Sum('cases_new'))['cases_new__sum']
        sum_deaths = obj.aggregate(Sum('cases_death'))['cases_death__sum']
        sum_recovery = obj.aggregate(Sum('cases_recovered'))['cases_recovered__sum']

        #sum = obj.aggregate(Sum('cases_new'))['cases_new__sum']
        return views.Response({'total_days':count, 'total_new_cases':sum_new_cases, 'total_deaths':sum_deaths, 'total_recovery':sum_recovery})


class ClusterPeriodSummaryView(views.APIView):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        state = request.query_params['state']
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']

        obj = Clusters.objects.filter(state=state, date_last_onset__gte=start_date, date_announced__lte=end_date)
        count = obj.count()

        #sum = obj.aggregate(Sum('cases_new'))['cases_new__sum']
        return views.Response({'count_active_clusters':count})

class TestsPeriodSummaryView(views.APIView):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        state = request.query_params['state']
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']

        obj = Tests.objects.filter(state=state, date__gte=start_date, date__lte=end_date)

        sum_rtk_ag = obj.aggregate(Sum('rtk_ag'))['rtk_ag__sum']
        sum_pcr = obj.aggregate(Sum('pcr'))['pcr__sum']

        return views.Response({'total_rtk_ag':sum_rtk_ag,'total_pcr':sum_pcr})

class CheckinsPeriodSummaryView(views.APIView):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        state = request.query_params['state']
        start_date = request.query_params['start_date']
        end_date = request.query_params['end_date']

        obj = MySJ.objects.filter(state=state, date__gte=start_date, date__lte=end_date)
        sum_checkins = obj.aggregate(Sum('checkins'))['checkins__sum']

        return views.Response({'total_checkins':sum_checkins})


class NewCasesRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Cases.objects.all().order_by('date')
    serializer_class = CasesRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class TotalCasesRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Cases.objects.all().order_by('date')
    serializer_class = TotalCasesRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class DeathRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Cases.objects.all().order_by('date')
    serializer_class = DeathRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class RecoveryRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = Cases.objects.all().order_by('date')
    serializer_class = RecoveryRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class CheckinsRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = MySJ.objects.all().order_by('date')
    serializer_class = CheckinsRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class IndCheckinsRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = MySJ.objects.all().order_by('date')
    serializer_class = IndCheckinsRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }

class CheckinLocationsRangeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows DailyNewCases to be viewed or edited.
    """
    queryset = MySJ.objects.all().order_by('date')
    serializer_class = CheckinLocationsRangeSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'state': ['exact'],
         'date': ['exact', 'lte', 'gte']
    }
