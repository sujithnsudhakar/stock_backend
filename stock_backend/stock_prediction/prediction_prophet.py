from fbprophet import Prophet
import pandas as pd
import csv
#from stock_business import StockAPI
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics

#from fbprophet.plot import plot_plotly

#Hardcoded variables to be passed on with pubsub
n_years = 5;
period = n_years * 365


#read_obj = StockAPI('', 'stock_value')
#response = read_obj.read_for_prediction()

#Temporary usage of data from csv file generaed form yfinance

#Data pre-processing
def preprocess_data(data_values):
    # Requires the date and its corressponding closing value
    df_train = data_values[['Date', 'Close']]
    # The date column should be populated under name 'ds' and closing value as 'y' according to the library req
    op_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
    #print(type(op_train['ds']))
    return op_train

# Predict forecast with Prophet.
def forecast_data(processed_data):
    #Creation of the Prophet model (m)
    model = Prophet()

    #Similiar to SKLearn, model fitting
    model.fit(processed_data)

    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)
    #print("Length is: ")
    #print(len(forecast.columns))
    return forecast



data = pd.read_csv (r'E:\Study\Semester 5\TDD\srccode\StockPredictionApp\DataLoadService\stock_data.csv')
#print (data[['Date', 'Close']])






data_preprocessed = preprocess_data(data)
#print(data_preprocessed)
#To be sent forward to next service (plot)
forecast_out = forecast_data(data_preprocessed)

forecast_length = len(forecast_out)


#Data post-processing
def postprocess_data(data_values):
    #Store the values in:
    dataSeries = []
    units = {}
    # Requires the date and its corressponding closing value
    df_train = data_values[['ds', 'yhat']]
    # The date column should be populated under name 'ds' and closing value as 'y' according to the library req
    op_train = df_train.rename(columns={"ds": "date", "yhat": "value"})
    #print(op_train)
    for index, row in op_train.iterrows():
        row1 = row['date'].strftime("%Y-%m-%d")
        #print(row1, row['value'])
        units['date'] = row1
        units['value'] = row['value']
        dataSeries.append(units)
    #print(dataSeries)
    return dataSeries


#print(forecast_out)

#print(len(forecast_out))

data_postprocessed = postprocess_data(forecast_out)
print(data_postprocessed)
# Cross-validation


def cross_validation(model):
    #model_cv = Prophet()
    #model_cv.fit(data_preprocessed)
    df_cv = cross_validation(model_cv, initial = '365 days', period = period/2, horizon = period)
    df_perf = performance_metrics(df_cv)

#To be sent to front end.
if __name__ == '__main__':
    data = forecast_out
    #data.to_csv('stock_data_prediction.csv')
    #print(type(forecast_out))
#print(forecast_out.tail())