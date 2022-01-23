from django.db import models
from core.models import State

class Cases(models.Model):
    date = models.DateField(db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    cases_new = models.IntegerField()
    cases_import = models.IntegerField()
    cases_recovered = models.IntegerField()
    cases_death = models.IntegerField()
    cases_active = models.IntegerField()
    cases_cluster = models.IntegerField()
    cases_unvax = models.IntegerField()
    cases_pvax = models.IntegerField()
    cases_fvax = models.IntegerField()
    cases_boost = models.IntegerField()
    cases_child = models.IntegerField()
    cases_adolescent = models.IntegerField()
    cases_adult = models.IntegerField()
    cases_elderly = models.IntegerField()

    def get_cases_new_per_population(self):
        return self.cases_new/(self.state.populations)

    def get_recoveries_per_population(self):
        return self.cases_recovered/(self.state.populations)

    def get_deaths_per_population(self):
        return self.cases_death/(self.state.populations)

    def get_active_cases_per_population(self):
        return self.cases_active/(self.state.populations)

class Clusters(models.Model):
    cluster =models.CharField(max_length=256)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    date_announced = models.DateField(db_index=True)
    date_last_onset = models.DateField(db_index=True)
    category = models.CharField(max_length=256)
    status = models.CharField(max_length=256)

class Tests(models.Model):
    date = models.DateField(db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    rtk_ag = models.IntegerField()
    pcr = models.IntegerField()

    def get_rtk_ag_per_population(self):
        return self.rtk_ag/(self.state.populations)

    def get_pcr_per_population(self):
        return self.pcr/(self.state.populations)

    def get_total_tests_per_population(self):
        return (self.rtk_ag+self.pcr)/(self.state.populations)

    def get_total_tests(self):
        return self.rtk_ag+self.pcr

class MySJ(models.Model):
    date = models.DateField(db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    checkins = models.IntegerField()
    unique_ind = models.IntegerField()
    unique_loc = models.IntegerField()
    checkins_to_ind_ratio = models.FloatField()
    checkins_to_unique_loc_ratio = models.FloatField()

    def get_unique_ind_per_population(self):
        return self.unique_ind/(self.state.populations)
