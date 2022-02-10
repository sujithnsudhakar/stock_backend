import sqlite3
from google.cloud import storage 
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys

#sql connection command
conn = mysql.connector.connect(user='root', password='MRCC_2021', host='34.134.79.209', database='Stocks')

def get_db_data():
    cursor = conn.cursor()
    cursor.execute("SELECT Stock_Code,Stock_name FROM STOCKS_LIST")
    #frame = pd.DataFrame(cursor.fetchall())
    #print(frame.head())
    records = cursor.fetchall()
    cursor.close()
    return records

def get_stocknames():
    company = []
    records = get_db_data()
    for row in records:
        company.append(row[1])
    company.pop(0) 
    return company   
