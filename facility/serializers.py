from .models import Hospital, ICU, PKRC
from rest_framework import serializers
from core.serializers import StateSerializer

class HospitalSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Hospital
        fields = [
            'date',
            'state',
            'beds',
            'beds_covid',
            'beds_noncrit',
            'admitted_pui',
            'admitted_covid',
            'admitted_total',
            'discharged_pui',
            'discharged_covid',
            'discharged_total',
            'hosp_covid',
            'hosp_pui',
            'hosp_noncovid',
            ]


class ICUSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = ICU
        fields = [
            'date',
            'state',
            'beds_icu',
            'beds_icu_rep',
            'beds_icu_total',
            'beds_icu_covid',
            'vent',
            'vent_port',
            'icu_covid',
            'icu_pui',
            'icu_noncovid',
            'vent_covid',
            'vent_pui',
            'vent_noncovid',
            'vent_used',
            'vent_port_used',
        ]


class PKRCSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = PKRC
        fields = [
            'date',
            'state',
            'beds',
            'admitted_pui',
            'admitted_covid',
            'admitted_total',
            'discharged_pui',
            'discharged_covid',
            'discharged_total',
            'pkrc_covid',
            'pkrc_pui',
            'pkrc_noncovid',
            ]
