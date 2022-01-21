from django.apps import AppConfig
from django.conf import settings

import os
import pickle

class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'
    MODEL_FILE = os.path.join(settings.MODELS, "covid_cases_regressor.pickle")
    with open(MODEL_FILE, 'rb') as file:
        model = pickle.load(file)
