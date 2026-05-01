import os
import sys
import pandas as pd
import mysql.connector

from dotenv import load_dotenv
load_dotenv()

from CREDITRISK.exception.exception import CREDITRISKException
from CREDITRISK.app_logger.logger import logging


# Load environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST", "127.0.0.1")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3307))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "1234")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "mydb")


class Creditdata:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE
            )
            logging.info("MySQL connection established")
        except Exception as e:
            raise CREDITRISKException(e, sys)

    # -------------------------------
    # CSV → DataFrame
    # -------------------------------
    def csv_to_dataframe(self, file_path):
        try:
            df = pd.read_csv(file_path)
            logging.info("CSV loaded successfully")
            return df
        except Exception as e:
            raise CREDITRISKException(e, sys)

    # -------------------------------
    # INSERT INTO MYSQL
    # -------------------------------
    def insert_data_mysql(self, df, table_name):
        try:
            cursor = self.connection.cursor()

            # Create table dynamically
            columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
            create_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})"
            cursor.execute(create_query)

            logging.info(f"Table {table_name} ready")

            # Insert data
            placeholders = ", ".join(["%s"] * len(df.columns))
            insert_query = f"INSERT INTO `{table_name}` VALUES ({placeholders})"

            data = [tuple(row) for row in df.values]

            cursor.executemany(insert_query, data)
            self.connection.commit()

            logging.info("Data inserted into MySQL successfully")

            return len(data)

        except Exception as e:
            raise CREDITRISKException(e, sys)
        



    # -------------------------------
    # EXTRACT FROM MYSQL
    # -------------------------------
    def extract_data_mysql(self, table_name):
        try:
            query = f"SELECT * FROM `{table_name}`"
            df = pd.read_sql(query, self.connection)

            logging.info(f"Data extracted from {table_name}")
            return df

        except Exception as e:
            raise CREDITRISKException(e, sys)

    # -------------------------------
    # CLOSE CONNECTION
    # -------------------------------
    def close_connection(self):
        try:
            self.connection.close()
            logging.info("MySQL connection closed")
        except Exception as e:
            raise CREDITRISKException(e, sys)


# -------------------------------
# MAIN TEST (like your style)
# -------------------------------
if __name__ == "__main__":
    FILE_PATH = "CREDITRISK/credit_data.csv"   # update path
    TABLE_NAME = "credit_data"

    obj = Creditdata()

    df = obj.csv_to_dataframe(FILE_PATH)
    print(df.head())

    count = obj.insert_data_mysql(df, TABLE_NAME)
    print("Inserted records:", count)

    extracted_df = obj.extract_data_mysql(TABLE_NAME)
    print(extracted_df.head())

    obj.close_connection()