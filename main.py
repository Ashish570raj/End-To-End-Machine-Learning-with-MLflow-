from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
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