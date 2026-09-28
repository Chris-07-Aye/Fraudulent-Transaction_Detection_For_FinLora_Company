import dagshub
import mlflow
import mlflow.sklearn


def setup_mlflow():

    Intializes MLflow tracking for project.

    dagshub.init(repo_owner='prinxlordstone', 
            repo_name='Fraudulent-Transaction_Detection_For_FinLora_Company', 
            mlflow=True)
    
   # Set experiment
    mlflow.set_experiment("Fraudulent_transaction_Detection_Models_For_Finlora") 