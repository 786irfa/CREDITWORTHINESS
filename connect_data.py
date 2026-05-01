import mysql.connector
import pandas as pd

try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="1234",
        database="mydb"
    )

    print("✅ Connected to MySQL Docker successfully")

    cursor = conn.cursor()

    # test query
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("Tables in DB:")
    for table in tables:
        print(table)

    conn.close()
    df = pd.read_csv(r"D:\creditworthiness\credit_data.csv")

    print("CSV Loaded Successfully")
    print(df.head())

# 2. Connect to MySQL (Docker)
    conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="1234",
    database="mydb"
)

    cursor = conn.cursor()



except Exception as e:
    print("❌ Error:", e)
