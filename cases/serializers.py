from .models import Cases, Clusters, Tests, MySJ
from rest_framework import serializers
from core.serializers import StateSerializer


class DailyCasesSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    def get_cases_new_per_population(self, obj):
        return obj.get_cases_new_per_population()

    def get_cases_recovered_per_population(self, obj):
        return obj.get_recoveries_per_population()

    def get_cases_death_per_population(self, obj):
        return obj.get_deaths_per_population()

    def get_cases_active_per_population(self, obj):
        #state = self.context["request"].query_params.get('state')
        return obj.get_active_cases_per_population()

    cases_new_per_population = serializers.SerializerMethodField()
    cases_recovered_per_population = serializers.SerializerMethodField()
    cases_death_per_population = serializers.SerializerMethodField()
    cases_active_per_population = serializers.SerializerMethodField()

    class Meta:
        model = Cases
        fields = [
            'date',
            #'state',
            'cases_new',
            'cases_recovered',
            'cases_death',
            'cases_active',
            'cases_new_per_population',
            'cases_recovered_per_population',
            'cases_death_per_population',
            'cases_active_per_population',
            ]

class DailyTestsSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)
    def get_total_tests(self, obj):
        return obj.get_total_tests()

    def get_rtk_ag_per_population(self, obj):
        return obj.get_rtk_ag_per_population()

    def get_pcr_per_population(self, obj):
        return obj.get_pcr_per_population()

    def get_total_tests_per_population(self, obj):
        return obj.get_total_tests_per_population()

    total_tests = serializers.SerializerMethodField()
    rtk_ag_per_population = serializers.SerializerMethodField()
    pcr_per_population = serializers.SerializerMethodField()
    total_tests_per_population = serializers.SerializerMethodField()

    class Meta:
        model = Tests
        fields = [
            'date',
            #'state',
            'rtk_ag',
            'pcr',
            'total_tests',
            'rtk_ag_per_population',
            'pcr_per_population',
            'total_tests_per_population',
            ]

class DailyCheckinsSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    def get_unique_ind_per_population(self, obj):
        return obj.get_unique_ind_per_population()

    unique_ind_per_population = serializers.SerializerMethodField()

    class Meta:
        model = MySJ
        fields = [
            'date',
            #'state',
            'checkins',
            'unique_ind',
            'unique_loc',
            'checkins_to_ind_ratio',
            'unique_ind_per_population',
            ]

class CasesRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)


    class Meta:
        model = Cases
        fields = [
            'date',
            'cases_new',
            ]

class TotalCasesRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = Cases
        fields = [
            'date',
            'cases_active',
            ]

class DeathRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = Cases
        fields = [
            'date',
            'cases_death',
            ]

class RecoveryRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = Cases
        fields = [
            'date',
            'cases_recovered',
            ]

class CheckinsRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = MySJ
        fields = [
            'date',
            'checkins',
            ]

class IndCheckinsRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = MySJ
        fields = [
            'date',
            'unique_ind',
            ]

class CheckinLocationsRangeSerializer(serializers.ModelSerializer):
    #state = StateSerializer(read_only=True)

    class Meta:
        model = MySJ
        fields = [
            'date',
            'unique_loc',
            ]


class ClustersSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Clusters
        fields = [
            'cluster',
            'state',
            'district',
            'date_announced',
            'date_last_onset',
            'category',
            'status',
            'cases_new',
            'cases_total',
            'cases_active',
            'tests',
            'icu',
            'deaths',
            'recovered',
            'summary_bm',
            'summary_en'
                ]


class TestsSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = Tests
        fields = [
            'date',
            'state',
            'rtk_ag',
            'pcr',
            ]


class MySJSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = MySJ
        fields = [
            'date',
            'state',
            'checkins',
            'unique_ind',
            'unique_loc',
        ]
