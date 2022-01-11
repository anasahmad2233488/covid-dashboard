from .models import Vaccination
from rest_framework import serializers
from core.serializers import StateSerializer

class VaccinationSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Vaccination
        fields = [
            'date',
            'state',
            'daily_partial',
            'daily_full',
            'daily',
            'daily_partial_child',
            'daily_full_child',
            'daily_booster',
            'cumul_partial',
            'cumul_full',
            'cumul',
            'cumul_partial_child',
            'cumul_full_child',
            'cumul_booster',
            'pfizer1',
            'pfizer2',
            'pfizer3',
            'sinovac1',
            'sinovac2',
            'sinovac3',
            'astra1',
            'astra2',
            'astra3',
            'sinopharm1',
            'sinopharm2',
            'sinopharm3',
            'cansino',
            'cansino3',
            'pending1',
            'pending2',
            'pending3',
            ]
