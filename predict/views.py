from django.shortcuts import render
from .apps import PredictConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictionListSerializer
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
        cases_active_avg = 'from model'

        # order of input [cn_1, cn_2, cn_3, cn_4, cn_5, temp_avg, checkins_avg, cases_active_avg, percent_vax]
        X = [1, 1, 1, 1, 1, 300, 30000, 26, 1., 1, 300, 30000, 26, 1., 1, 300, 30000]
        X = np.array(X).reshape(1,-1)

        # choose model
        model = PredictConfig.model[int(state)]

        # Predict for n number of days. Each time, shift the new cases input
        result_list = []
        for i in range(10):
            y = float(model.predict(X))
            for j in range(4):
                X[0][j] = X[0][j+1]
            X[0][4] = y
            date = date + pd.tseries.offsets.DateOffset(days=1)
            result_list.append({'name':'predicted', 'cases_new':y, 'date':str(date)[:10]})

        date = date - pd.tseries.offsets.DateOffset(days=40)
        for i in range(35):
            y = float(model.predict(X))
            for j in range(4):
                X[0][j] = X[0][j+1]
            X[0][4] = y-100
            date = date + pd.tseries.offsets.DateOffset(days=1)
            result_list.append({'name':'actual', 'cases_new':y, 'date':str(date)[:10]})

        # transform output


        return Response(result_list)
