import os
import sys
import numpy as np
import pandas as pd
target_column=target_column="Target"

pipeline_name :str ="CREDITRISK"
artifact_dir:str ="artifacts"
'''
data ingestion related constant start with data ingestion variable name
'''

data_ingestion_table_name: str = "credit_data"
data_ingestion_database_name: str = "IRFANAI"
data_ingestion_dir_name:str = "data_ingestion"
data_ingestion_feature_store_dir:str = "feature_store"
data_ingestion_ingested_dir:str ="ingested"
data_ingestion_train_test_split_ratio:float=0.2
data_ingestion_processed_data_dir: str = "processed_data"
data_ingestion_file_name: str = "credit_data.csv"
data_ingestion_mysql_uri_env_var: str = "MYSQL_URI"
train_file_name="training"
test_file_name="testing"