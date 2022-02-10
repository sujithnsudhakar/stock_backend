import pytest
import main

@pytest.fixture
def test_get_db_data():
    records = main.get_db_data()
    assert len(records) != 0

@pytest.fixture
def test_get_stocknames():
    records = main.get_stocknames()
    assert len(company) != 0