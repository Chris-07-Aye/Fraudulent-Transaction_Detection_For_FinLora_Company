import mlflow.sklearn
import mlflow
from src.utility.mlflow_setup import setup_mlflow

def load_register_model():

    load registered model from mlflow

    setup_mlflow()

    model_name = "Fraud_Detection_XGBoost_Pipeline"
    model_version = "latest"

    model_uri = f"models:/{model_name}/{model_version}"
    model = mlflow.sklearn.load_model(model_uri)

    return model


#load_register_model()