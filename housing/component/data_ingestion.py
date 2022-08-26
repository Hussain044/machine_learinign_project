from housing.entity.config_entity import DataIngestionConfig
from housing.exception import HousingException
import sys, os
from housing.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config):
        try:
            logging.info("")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys)

    def initate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys)