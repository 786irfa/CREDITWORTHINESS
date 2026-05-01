from CREDITRISK.components.data_ingestion import DataIngestion
from CREDITRISK.exception.exception import CREDITRISKException
from CREDITRISK.app_logger.logger import logging
from CREDITRISK.entity.config_entity import DataIngestionConfig
from CREDITRISK.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        print("🚀 Pipeline started")

        # ✅ Step 1: Pipeline config
        training_pipeline_config = TrainingPipelineConfig()

        # ✅ Step 2: Data ingestion config
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)

        # ✅ Step 3: Data ingestion component
        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Initiating data ingestion")

        # ✅ Step 4: Run ingestion
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        print("✅ Data Ingestion Completed")
        print(data_ingestion_artifact)

    except Exception as e:
        logging.error("Error occurred in main pipeline")
        raise CREDITRISKException(e, sys)