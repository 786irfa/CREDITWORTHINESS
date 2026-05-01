from datetime import datetime
import os

from CREDITRISK.constant import training_pipeline


# =========================
# TRAINING PIPELINE CONFIG
# =========================
class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):

        # ✅ Basic identifiers
        self.pipeline_name = training_pipeline.pipeline_name
        self.artifact_root = training_pipeline.artifact_dir

        # ✅ Timestamp for unique runs
        self.timestamp: str = timestamp.strftime("%Y%m%d%H%M%S")

        # ✅ FINAL artifact directory (IMPORTANT FIX)
        self.artifact_dir = os.path.join(
            self.artifact_root,
            self.timestamp,
            self.pipeline_name
            
        )
        

        # 🔥 CREATE DIRECTORY
        os.makedirs(self.artifact_dir, exist_ok=True)



# =========================
# DATA INGESTION CONFIG
# =========================
class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):

        # ✅ Root ingestion folder
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.data_ingestion_dir_name
        )

        # 🔥 CREATE ingestion directory
        os.makedirs(self.data_ingestion_dir, exist_ok=True)

        # ✅ Feature store path
        self.data_ingestion_feature_store: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_feature_store_dir,
            training_pipeline.data_ingestion_file_name
        )

        # 🔥 CREATE feature store folder
        os.makedirs(os.path.dirname(self.data_ingestion_feature_store), exist_ok=True)

        # ✅ Ingested train/test folder
        ingested_dir = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_ingested_dir
        )   

        

        # 🔥 CREATE ingested folder
        os.makedirs(ingested_dir, exist_ok=True)

        # ✅ Train file
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_ingested_dir,
            training_pipeline.train_file_name
        )

        # ✅ Test file
        self.testing_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.data_ingestion_ingested_dir,
            
            training_pipeline.test_file_name
        )

        # ✅ Split ratio
        self.train_test_split: float = (
            training_pipeline.data_ingestion_train_test_split_ratio
        )
        self.train_test_split: float = training_pipeline.data_ingestion_train_test_split_ratio
        self.table_name: str = training_pipeline.data_ingestion_table_name
        self.database_name: str = training_pipeline.data_ingestion_database_name



        print(f"[INFO] Data ingestion dir created: {self.data_ingestion_dir}")