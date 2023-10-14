from pathlib import Path
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger

STAGE_NAME = "Data Transformation stage"

class dataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"), 'r') as f:
                status = f.read().split(" ")[-1]
                print(status)

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your data schema is not valid")
            
        except Exception as e:
            print(e)
