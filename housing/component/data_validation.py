from logging import raiseExceptions
from housing.config.configuration import Configuration
from housing.entity.config_entity import DataValidationConfig
from housing.exception import HousingException
from housing.logger import logging
import sys
import os
from housing.entity.artifact_entity import DataIngestionArtifact


class DataValidataion:
    def __init__(self, data_validation_config: DataValidationConfig,
                 data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

        except Exception as e:
            raise HousingException(e, sys) from e

    def is_train_test_file_exists(self):
        try:
            logging.info(f"Checking if training and testing data is available")
            is_train_file_exist = False
            is_test_file_exits = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exits = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exits

            logging.info(f"Is train and data file exists?-> {is_available}")

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                message = f"Training file: {training_file} or Testing file: {testing_file}"\
                    "is not present"
                raise Exception(message)

            return is_available

        except Exception as e:
            raise HousingException(e, sys) from e

    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False
            # Assignment validate training and testing dataset using schema file
            # 1. Number of Column
            # 2. Check the value of ocean proximity
            # acceptable values
            # 3. Check column names

            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e

    def initiate_data_validation(self):
        try:
            is_available = self.is_train_test_file_exists()
            validation_status = self.validate_dataset_schema()

        except Exception as e:
            raise HousingException(e, sys) from e
