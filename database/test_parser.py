import pytest
from parser import get_data_from_avito


def test_avito():
    assert get_data_from_avito() == 'data'
    assert get_data_from_avito() == 'data'
