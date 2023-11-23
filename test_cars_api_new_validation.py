import os
import unittest
import pytest
from assertpy import assert_that, soft_assertions, fail
import requests
import json


@pytest.fixture(scope='module')
def test_load_api():
    body = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
    response = json.loads(body.text)


def test_api_status_code(test_load_api):
    print(test_load_api.json()['Status'])
    assert_that(test_load_api['Headers']).is_equal_to(87)