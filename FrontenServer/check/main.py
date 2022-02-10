import sqlite3
from google.cloud import storage 
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys

conn = mysql.connector.connect(user='root', password='MRCC_2021', host='34.134.79.209', database='Stocks')

def get_stocknames():
    cursor = conn.cursor()
    cursor.execute("SELECT Stock_Code, Stock_name FROM STOCKS_LIST")
    # frame = pd.DataFrame(cursor.fetchall())
    # print(frame.head())
    records = cursor.fetchall()
    for row in records:
        print("code", row[0])
        print("name", row[1])
    cursor.close()
    return records

get_stocknames()