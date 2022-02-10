import pytest
import main

def test_get_stocknames():
    records = main.get_stocknames()
    assert len(records) == 0, "test failed"
