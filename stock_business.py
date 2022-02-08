import typing
from unittest import result
import yfinance as yf
import pandas as pd
from datetime import date
import json
import time
import datetime
from pymongo import MongoClient
from flask import Flask, request, json, Response

class StockAPI:  
    def __init__(self, data, mongo_collection):   # Fetchs the MongoDB connection
        self.client = MongoClient("mongodb+srv://root:root@clusterstock.j0wyt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        database = 'stock_info'
        collection = mongo_collection
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def insert_data(self, data):    
        response = self.collection.insert_many(data)
        output = {'Status': 'Successfully Inserted'}
        return output

    def read_all(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

def select_stock_data_for_company(company: str):
    read_obj = StockAPI('', 'stock_value')
    response = read_obj.read_all()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')
    

def get_stock_info(company:str):
    response = select_stock_data_for_company(company)
    return response
    
def load_data(company:str, start_date, end_date):
    data = yf.download(company, start_date, end_date)
    data.reset_index(inplace=True)
    return data


def persist_fin_data():
    # TODO get the company and start_date from request param only if we are planning to give an interface
    # company = request.args.get('company')
    company = "GOOG"
    start_date = "2015-01-01"
    end_date = date.today().strftime("%Y-%m-%d")
    stock_df  = load_data(company, start_date, end_date)
    stock_json = stock_df.to_dict('records')
    create_obj = StockAPI(stock_json, 'stock_value')
    response = create_obj.insert_data(stock_json)
    return response