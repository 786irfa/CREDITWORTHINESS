import os
import sys
import pandas as pd

from CREDITRISK.exception.exception import CREDITRISKException
from CREDITRISK.app_logger.logger import logging

from CREDITRISK.push_data import Creditdata   # importing your class


class ReadData:
    def __init__(self):
        try:
            self.obj = Creditdata()
            logging.info("ReadData initialized successfully")
        except Exception as e:
            raise CREDITRISKException(e, sys)

    # -------------------------------
    # READ DATA FROM MYSQL
    # -------------------------------
    def read_from_mysql(self, table_name):
        try:
            df = self.obj.extract_data_mysql(table_name)
            logging.info("Data read successfully from MySQL")
            return df

        except Exception as e:
            raise CREDITRISKException(e, sys)

    # -------------------------------
    # CLOSE CONNECTION
    # -------------------------------
    def close(self):
        try:
            self.obj.close_connection()
            logging.info("Connection closed in read module")
        except Exception as e:
            raise CREDITRISKException(e, sys)


# -------------------------------
# MAIN TEST
# -------------------------------
if __name__ == "__main__":

    TABLE_NAME = "credit_data"

    reader = ReadData()

    df = reader.read_from_mysql(TABLE_NAME)

    print("===== DATA PREVIEW =====")
    print(df)

    print("\nTotal Rows:", len(df))

    reader.close()