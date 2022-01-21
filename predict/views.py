from django.shortcuts import render
from .apps import PredictConfig
from rest_framework.views import APIView
from rest_framework.response import Response

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class predictCasesView(APIView):
    def get(request):
        state = request.GET.get('state')
        percent_vax = request.GET.get('percent_vax')
        temp_avg = request.GET.get('temp_avg')
        checkins_avg = request.GET.get('checkins_avg')

        # transform input
        cases_active_avg = 'from model'

        # order of input [cn_1, cn_2, cn_3, cn_4, cn_5, temp_avg, checkins_avg, cases_active_avg, percent_vax]
        X = ['cn_1', 'cn_2', 'cn_3', 'cn_4', 'cn_5', 'cases_active_avg', 'checkins_avg', 'temp_avg', 'percent_vax']
        X = np.array(X).reshape(1,-1)

        # choose model
        model = PredictConfig.model[state]

        # Predict for n number of days. Each time, shift the new cases input
        result = []
        for i in range(10):
            y = float(model.predict(X))
            for j in range(4):
                X[0][j] = X[0][j+1]
            X[0][4] = y
            result.append(y)

        # transform output



        return render(result)
