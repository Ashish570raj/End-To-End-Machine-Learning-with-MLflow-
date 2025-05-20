from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from mlproject.pipeline.stage_2_data_validation import DataValidationTraningPipeline 
from mlproject.pipeline.stage_03_data_transformation import DataTransformationTraningPipeline 
from mlproject.pipeline.stage_04_model_trainer import MOdelTraningPipeline 
from mlproject.pipeline.stage_05_model_evaluation import MOdelEvaluationTraningPipeline 
# logger.info("welcome to our custom login")


STAGE_NAME="Data Ingestion stage"

# if __name__ =="__main__":
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj=DataIngestionTraningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
except Exception as e:
    logger.exceptiona(e)
    raise e


STAGE_NAME="Data validation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj=DataValidationTraningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
except Exception as e:
    logger.exceptiona(e)
    raise e



STAGE_NAME="Data transformation stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
    obj=DataTransformationTraningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
except Exception as e:
    logger.exceptiona(e)
    raise e


STAGE_NAME="Model Trainer stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=MOdelTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
except Exception as e:
        logger.exceptiona(e)
        raise e 


STAGE_NAME="Model Evaluation stage"
try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=MOdelEvaluationTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
except Exception as e:
        logger.exceptiona(e)
        raise e 