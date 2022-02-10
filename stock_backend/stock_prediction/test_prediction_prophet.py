import pytest
import pandas
import prediction_prophet

def test_preprocess_data():
    result = prediction_prophet.preprocess_data(prediction_prophet.data)
    assert type(result) is pandas.core.frame.DataFrame
    assert len(result.columns) == 2
    assert result.columns[0] == 'ds'
    assert result.columns[1] == 'y'

def test_forecast_data():
    result = prediction_prophet.forecast_data(prediction_prophet.data_preprocessed)
    assert type(result) is pandas.core.frame.DataFrame
    assert len(result.columns) == 19