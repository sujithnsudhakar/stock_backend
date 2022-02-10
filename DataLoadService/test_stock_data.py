import pytest
import main

@pytest.fixture
def test_load_data(ticker):
    data = main.load_data()
    assert len(data) != 0