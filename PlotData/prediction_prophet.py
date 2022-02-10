
from fbprophet import Prophet
import pandas as pd

#from fbprophet.plot import plot_plotly

#Hardcoded variables to be passed on with pubsub
n_years = 5;
period = n_years * 365

#Temporary usage of data from csv file generaed form yfinance

# Predict forecast with Prophet.
data = pd.read_csv (r'D:\OneDrive\Documents\Documents\OvGU\WiSe 21-22\Stock Prediction App\StockPredictionApp\DataLoadService\stock_data.csv')
#print (data[['Date', 'Close']])



#Requires the date and its corressponding closing value
df_train = data[['Date', 'Close']]
#The date column should be populated under name 'ds' and closing value as 'y' according to the library req
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

print(df_train)


#Creation of the Prophet model (m)
m = Prophet()
#Similiar to SKLearn, model fitting
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

print(forecast.tail())

import plotly.graph_objects as go
fig = go.Figure([go.Scatter(x=data['Date'], y=data['High'])])
fig = go.Figure([go.Scatter(x=forecast['ds'], y=forecast['yhat'])])
fig.show()