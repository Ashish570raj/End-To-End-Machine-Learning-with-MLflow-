from mlproject.config.configuration import ConfigurationManager
# from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger
from pathlib import Path

STAGE_NAME="Model Evaluation stage"

class MOdelEvaluationTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        
if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=MOdelEvaluationTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
    except Exception as e:
        logger.exceptiona(e)
        raise e 