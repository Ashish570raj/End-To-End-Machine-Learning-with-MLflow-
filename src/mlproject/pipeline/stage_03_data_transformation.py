from mlproject.config.configuration import ConfigurationManager
# from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path

STAGE_NAME="Data transformation stage"

class DataTransformationTraningPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r")as f:
                status =f.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config= config.get_data_transformation_config()
                data_transformation= DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("your data schema is invalid")
        
        except Exception as e:
            print(e)
        
    
if __name__ =="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj=DataTransformationTraningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} has completed <<<<<\n\n x========================================x")
    except Exception as e:
        logger.exceptiona(e)
        raise e 