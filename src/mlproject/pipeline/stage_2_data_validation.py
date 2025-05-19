from mlproject.config.configuration import ConfigurationManager
# from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME="Data validation stage"

class DataValidationTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
       config = ConfigurationManager()
       data_validation_config = config.get_data_validation_config()
       data_validation = DataValidation(config=data_validation_config)
       data_validation.validate_all_columns()
       
if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=DataValidationTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
    except Exception as e:
        logger.exceptiona(e)
        raise e 
    