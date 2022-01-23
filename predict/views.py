from django.shortcuts import render
from .apps import PredictConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from cases.models import Cases
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class predictCasesView(APIView):
    def get(self, request):
        state = request.GET.get('state')
        date = pd.to_datetime(request.GET.get('date'))
        percent_vax = request.GET.get('percent_vax')
        temp_avg = request.GET.get('temp')
        checkins_avg = request.GET.get('checkins')

        # transform input
        date_0 = date - pd.tseries.offsets.DateOffset(days=30)
        date_1 = date + pd.tseries.offsets.DateOffset(days=10)
        cases = Cases.objects.filter(state=state, date__gte=date_0, date__lte=date_1)

        result_list = []
        for case in cases:
            result_list.append({'name':'actual', 'cases_new':case.cases_new, 'date':case.date})

        cases_active_avg = 0
        population = cases[0].state.populations

        X = []
        date_0 = date - pd.tseries.offsets.DateOffset(days=5)
        for i in range(5):
            X += [Cases.objects.get(state=state, date=date_0).cases_new]
            cases_active_avg += cases[0].cases_active
            date_0 = date_0 + pd.tseries.offsets.DateOffset(days=1)

        cases_active_avg /= 5

        # order of input [cn_1, cn_2, cn_3, cn_4, cn_5, temp_avg, checkins_avg, cases_active_avg, percent_vax]
        X += [float(temp_avg), float(checkins_avg)*population/100, float(cases_active_avg), float(percent_vax)/100]
        X = np.array(X).reshape(1,-1)

        # choose model
        model = PredictConfig.model['cases'][int(state)]

        # Predict for n number of days. Each time, shift the new cases input
        for i in range(10):
            y = int(model.predict(X))
            for j in range(4):
                X[0][j] = X[0][j+1]
            X[0][4] = y
            date = date + pd.tseries.offsets.DateOffset(days=1)
            result_list.append({'name':'predicted', 'cases_new':y, 'date':str(date)[:10]})

        return Response(result_list)

class predictDeathView(APIView):
    def get(self, request):
        state = request.GET.get('state')
        date = pd.to_datetime(request.GET.get('date'))
        percent_vax = request.GET.get('percent_vax')
        temp_avg = request.GET.get('temp')
        checkins_avg = request.GET.get('checkins')

        # transform input
        date_0 = date - pd.tseries.offsets.DateOffset(days=30)
        date_1 = date + pd.tseries.offsets.DateOffset(days=10)
        cases = Cases.objects.filter(state=state, date__gte=date_0, date__lte=date_1)

        result_list = []
        for case in cases:
            result_list.append({'name':'actual', 'cases_death':case.cases_death, 'date':case.date})

        cases_active_avg = 0
        population = cases[0].state.populations

        X = []
        date_0 = date - pd.tseries.offsets.DateOffset(days=5)
        for i in range(5):
            X += [int(Cases.objects.get(state=state, date=date_0).cases_new)]
            cases_active_avg += cases[0].cases_active
            date_0 = date_0 + pd.tseries.offsets.DateOffset(days=1)

        cases_active_avg /= 5

        # order of input [cn_1, cn_2, cn_3, cn_4, cn_5, temp_avg, checkins_avg, cases_active_avg, percent_vax]
        X_cases = X + [float(temp_avg), float(checkins_avg)*population/100, float(cases_active_avg), float(percent_vax)/100]
        X_cases = np.array(X_cases).reshape(1,-1)

        X_death = X + [float(cases_active_avg)]
        X_death = np.array(X_death).reshape(1,-1)

        # choose model
        model_cases = PredictConfig.model['cases'][int(state)]
        model_death = PredictConfig.model['death'][int(state)]

        # Predict for n number of days. Each time, shift the new cases input
        for i in range(10):
            y = abs(int(model_death.predict(X_death)))
            for j in range(4):
                X_death[0][j] = X_death[0][j+1]
                X_cases[0][j] = X_cases[0][j+1]
            y_cases = int(model_cases.predict(X_cases))
            X_cases[0][4] = y_cases
            X_death[0][4] = y_cases
            date = date + pd.tseries.offsets.DateOffset(days=1)
            result_list.append({'name':'predicted', 'cases_death':y, 'date':str(date)[:10]})

        return Response(result_list)
