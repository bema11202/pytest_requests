import os
import unittest
import pytest
from assertpy import assert_that, soft_assertions, fail
import requests


@pytest.fixture(scope='module')
def test_load_api():
    response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
    return response


def test_api_status_code(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)


def test_api_response_time(test_load_api):
    assert_that(test_load_api.elapsed.total_seconds()).is_less_than(1)


def test_api_response_content(test_load_api):
    print(test_load_api.headers['Content-Type'])
    assert_that(test_load_api.headers['Content-Type']).is_equal_to('application/json')


def test_api_response_content_length(test_load_api):
    print(test_load_api.headers['Content-Length'])
    assert_that(test_load_api.headers['Content-Length']).is_equal_to('3620')


def test_api_response_content_encoding(test_load_api):
    assert_that(test_load_api.headers['Content-Encoding']).is_equal_to('gzip')


def test_api_response_content_server(test_load_api):
    assert_that(test_load_api.headers['Server']).is_equal_to('Microsoft-IIS/10.0')


def test_api_response_content_access_control_allow_origin(test_load_api):
    print(test_load_api.headers)
    assert_that(test_load_api.headers['Access-Control-Expose-Headers']).is_equal_to('Request-Context')


def test_api_response_content_access_control_max_age(test_load_api):
    assert_that(test_load_api.headers['Strict-Transport-Security']).is_equal_to(
        'max-age=31536000 ; includeSubDomains ; preload')


def test_api_response_content_access_control_expose_headers(test_load_api):
    print(test_load_api.headers['Access-Control-Expose-Headers'])
    assert_that(test_load_api.headers['Access-Control-Expose-Headers']).is_equal_to('Request-Context')
