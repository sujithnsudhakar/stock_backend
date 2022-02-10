from logging import debug
from flask import Flask, render_template, jsonify
from flask import request
from stock_business import get_stock_info, load_data, persist_fin_data
from flask_cors import CORS

import json

import pandas as pd


app = Flask(__name__)

CORS(app)


@app.route('/')
def index():
    return "success"
    # return render_template('home.html')

@app.route('/getStocks')
def get_stocks():
    # fetch vals from query param ?company=some-value&stock_dt="2021-11-12 00:00:00"
    # sample request http://127.0.0.1:5000/getStocks?company=GOOG&stock_dt=2021-11-12%2000:00:00
    company = request.args.get('company')
    return get_stock_info(company)

@app.route('/persistfindata')
def load_stocks_info_into_db():
    response = persist_fin_data()
    return response


if __name__ == '__main__':
    app.run(debug=True)