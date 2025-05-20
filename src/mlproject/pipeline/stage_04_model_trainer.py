from mlproject.config.configuration import ConfigurationManager
# from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger
from pathlib import Path

STAGE_NAME="Model Trainer stage"

class MOdelTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config= config.get_model_trainer_config()
        data_transformation= ModelTrainer(config=data_transformation_config)
        data_transformation.train()
        
        
if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=MOdelTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
    except Exception as e:
        logger.exceptiona(e)
        raise e 