# Import yfinance packages to fetch the data
from datetime import date
import pandas as pd

import yfinance as yf

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

#st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')


#@st.cache
def load_data(ticker):
    #To get the data from yahoo finance from Start till today (already in Pandas dataframe)
    data = yf.download(ticker, START, TODAY)
    #The The index will be the first column the frame(data in this scenario)
    data.reset_index(inplace=True)
    return data


if __name__ == '__main__':
    data = load_data('GOOG')
    data.to_csv('stock_data.csv')