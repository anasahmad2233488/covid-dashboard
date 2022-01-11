from django.db import models
from core.models import State

class Hospital(models.Model):
    date = models.DateField(db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    beds = models.IntegerField()
    beds_covid = models.IntegerField()
    beds_noncrit = models.IntegerField()
    admitted_pui = models.IntegerField()
    admitted_covid = models.IntegerField()
    admitted_total = models.IntegerField()
    discharged_pui = models.IntegerField()
    discharged_covid = models.IntegerField()
    discharged_total = models.IntegerField()
    hosp_covid = models.IntegerField()
    hosp_pui = models.IntegerField()
    hosp_noncovid = models.IntegerField()


class ICU(models.Model):
    date = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    beds_icu = models.IntegerField()
    beds_icu_rep = models.IntegerField()
    beds_icu_total = models.IntegerField()
    beds_icu_covid = models.IntegerField()
    vent = models.IntegerField()
    vent_port = models.IntegerField()
    icu_covid = models.IntegerField()
    icu_pui = models.IntegerField()
    icu_noncovid = models.IntegerField()
    vent_covid = models.IntegerField()
    vent_pui = models.IntegerField()
    vent_noncovid = models.IntegerField()
    vent_used = models.IntegerField()
    vent_port_used = models.IntegerField()


class PKRC(models.Model):
    date = models.DateField(db_index=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    beds = models.IntegerField()
    admitted_pui = models.IntegerField()
    admitted_covid = models.IntegerField()
    admitted_total = models.IntegerField()
    discharged_pui = models.IntegerField()
    discharged_covid = models.IntegerField()
    discharged_total = models.IntegerField()
    pkrc_covid = models.IntegerField()
    pkrc_pui = models.IntegerField()
    pkrc_noncovid = models.IntegerField()
