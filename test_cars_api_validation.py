import os
import unittest
import pytest
from assertpy import assert_that, soft_assertions, fail
import requests

@pytest.fixture(scope='module')
def test_load_api():
    response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
    return response

def test_find_all_manufacturers(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    print(all_manufacturers[0])
    assert_that(all_manufacturers[0]['Mfr_Name']).is_equal_to("TESLA, INC.")
    assert_that(all_manufacturers[0]['Country']).is_equal_to("UNITED STATES (USA)")



def test_find_all_car_models(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    assert_that(test_load_api.elapsed.total_seconds()).is_less_than(1)
    assert_that(len(test_load_api.json())).is_greater_than(0)
    assert_that(len(test_load_api.json())).is_less_than(1000)