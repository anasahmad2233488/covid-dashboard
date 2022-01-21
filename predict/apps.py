from django.apps import AppConfig
import pickle

class PredictConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'predict'
    MODEL_FILE = os.path.join(settings.MODELS, "covid_cases_regressor.pickle")
    model = pickle.load(MODEL_FILE)
