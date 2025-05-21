from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger
from pathlib import Path

from dotenv import load_dotenv
import mlflow
import os

STAGE_NAME = "Model Trainer stage"

class MOdelTraningPipeline:
    def __init__(self):
        # Load environment variables from .env
        load_dotenv()

        # Configure MLflow from .env
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
        mlflow.set_tracking_username(os.getenv("MLFLOW_TRACKING_USERNAME"))
        mlflow.set_tracking_password(os.getenv("MLFLOW_TRACKING_PASSWORD"))

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_model_trainer_config()
        data_transformation = ModelTrainer(config=data_transformation_config)
        data_transformation.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = MOdelTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
    except Exception as e:
        logger.exception(e)
        raise e
