import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_enity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_enity import TrainingPipelineConfig

if __name__ == '__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataIngestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataIngestionconfig)
        logging.info("Starting Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info(f"Data Ingestion completed and artifact: {dataingestionartifact}")
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)


    except Exception as e:
        raise NetworkSecurityException(e,sys)