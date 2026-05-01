from  CREDITRISK.exception.exception import CREDITRISKException
from CREDITRISK.app_logger.logger import logging
###configuration of the dsataingestionconfig
from  CREDITRISK.entity.config_entity import DataIngestionConfig
import os
import sys
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split
import pandas  as pd
from CREDITRISK.entity.Artifact_entity import DataIngestionArtifact

from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv("Mysql_uri")
###creating dataingestionclass
class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise CREDITRISKException(e,sys)
    def export_table_as_dataframe(self):
        """THIS Function is only for reading the data from the mysql"""
        try:
            database_name=self.data_ingestion_config.database_name
            table_name=self.data_ingestion_config.table_name
            self.Mysql_url = "mysql+pymysql://root:1234@127.0.0.1:3307/mydb"
            import sqlalchemy
            engine = sqlalchemy.create_engine(self.Mysql_url)

            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, engine)

            return df

        except Exception as e:
            raise CREDITRISKException(e,sys)
        ##this function is for converting or shifting data into feature store 
    def export_data_into_feature_store(self,dataframe:pd.DataFrame):
        try:
            data_feature_store_file_path=self.data_ingestion_config.data_ingestion_feature_store
            ##creating folder 
            dir_path=os.path.dirname(data_feature_store_file_path) 
            os.makedirs(dir_path,exist_ok=True) 
            dataframe.to_csv(data_feature_store_file_path)  
            return dataframe
        except Exception as e:
            raise CREDITRISKException(e,sys) 
    ##this function is for train and test split 
    def split_as_train_test(self,dataframe:pd.DataFrame):
        try:
            train_set,test_set=train_test_split(dataframe,
            test_size=self.data_ingestion_config.train_test_split)
            logging.info("performed train test split on the dataframe")
            logging.info("exited split_data_as_train_test method of data_ingestion class")
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info("exporting train and test file path")

            train_set.to_csv(self.data_ingestion_config.training_file_path,
                             index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)
            logging.info(f"exported train and test file path")
        except Exception as e:

            raise CREDITRISKException(e,sys)
    def initiate_data_ingestion(self):
        try:
        
            dataframe =self.export_table_as_dataframe()
            dataframe=self.export_data_into_feature_store(dataframe)
            self.split_as_train_test(dataframe)
            dataingestionartifact=DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                        test_file_path=self.data_ingestion_config.testing_file_path)
            return dataingestionartifact
        except Exception as e:
            raise CREDITRISKException(e,sys)
        


