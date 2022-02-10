from datetime import date
import pandas as pd
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
import numpy as np
from pmdarima import auto_arima
# Ignore harmless warnings
import warnings
warnings.filterwarnings("ignore")
from statsmodels.tsa.arima.model import ARIMA

def load_data():
  df=pd.read_csv('stock_data.csv',index_col='Date',parse_dates=True)
  df.drop('Unnamed: 0', axis=1, inplace=True)
  df=df.dropna()
  return df

def calc_accuracy(df):
  traindata_size = int(df.shape[0] * 0.9)

  train, test = model_selection.train_test_split(df, train_size=traindata_size)
  testing_data = list(df[traindata_size:]['Close'])
  training_data = list(df[0:traindata_size]['Close'])
  warnings.filterwarnings("ignore")
  stepwise_fit = auto_arima(df.Close, 
                          suppress_warnings=True)           
  p = stepwise_fit.order[0]
  q = stepwise_fit.order[2]
  d = stepwise_fit.order[1]
  model_predictions = []
  n_test_obs = len(test)
  for i in range(n_test_obs):
    model = ARIMA(training_data,order=(p,d,q))
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    model_predictions.append(yhat)
    actual_test_value = testing_data[i]
    training_data.append(actual_test_value)

  mape = np.mean(np.abs(np.array(model_predictions) - np.array(testing_data))/ np.abs(testing_data)) #mean absolute percentage error
  accuracy = 100 - int(mape * 100)
  return accuracy

def forecast_data(df):
  stepwise_fit = auto_arima(df.Close, 
                          suppress_warnings=True)           
  p = stepwise_fit.order[0]
  q = stepwise_fit.order[2]
  d = stepwise_fit.order[1]
  model=ARIMA(df.Close, order=(p,d,q))
  result=model.fit()
  index_future_dates=pd.date_range(start='2022-01-12',end='2022-02-11')
  pred=result.predict(start=len(df),end=len(df)+30,typ='levels').rename('ARIMA predictions')
  pred.index=index_future_dates

  return pred

data = load_data()
accuracy = calc_accuracy(data)
forecasted_values = forecast_data(df)

#To be sent to front end.
if __name__ == '__main__':
    data = forecasted_values
    arima_accuracy = accuracy
  
