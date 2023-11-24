import os
import unittest
import pytest
from assertpy import assert_that, soft_assertions, fail
import requests
import json


@pytest.fixture(scope='module')
def test_load_api():
    response = requests.get('https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json')
    return response


def test_find_all_manufacturers(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    for manufacturer in all_manufacturers:
        print(manufacturer['Mfr_Name'])
        assert_that(manufacturer['Mfr_Name']).is_not_none()
        assert_that(manufacturer['Mfr_Name']).is_not_empty()
        assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_usa(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "UNITED STATES (USA)":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_mexico(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print("*" * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "MEXICO":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_canada(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "CANADA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_germany(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "GERMANY":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_italy(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "ITALY":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_france(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "FRANCE":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_japan(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "JAPAN":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_south_korea(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SOUTH KOREA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_sweden(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SWEDEN":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_united_kingdom(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "UNITED KINGDOM":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_spain(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SPAIN":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_india(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "INDIA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_china(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "CHINA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_taiwan(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "TAIWAN":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_thailand(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "THAILAND":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_turkey(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "TURKEY":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_czech_republic(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "CZECH REPUBLIC":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_brazil(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "BRAZIL":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_slovakia_(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SLOVAKIA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_slovenia_(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SLOVENIA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_all_manufacturers_in_south_africa_(test_load_api):
    all_manufacturers = test_load_api.json()['Results']
    assert_that(test_load_api.status_code).is_equal_to(200)
    print('*' * 20)
    for manufacturer in all_manufacturers:
        if manufacturer['Country'] == "SOUTH AFRICA":
            print(manufacturer['Mfr_Name'])
            assert_that(manufacturer['Mfr_Name']).is_not_none()
            assert_that(manufacturer['Mfr_Name']).is_not_equal_to('')


def test_find_the_number_of_cars_available(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    count = test_load_api.json()["Count"]
    assert_that(count).is_equal_to(87)


def test_find_the_cars_api_message(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    message = test_load_api.json()["Message"]
    assert_that(message).is_equal_to("Response returned successfully")


def test_find_the_cars_api_search_criteria(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    search_criteria = test_load_api.json()["SearchCriteria"]
    assert_that(search_criteria).is_equal_to(None)


def test_find_cars_manufacturers(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[0]["Mfr_ID"]).is_equal_to(955)
    assert_that(results[0]["Mfr_Name"]).is_equal_to("TESLA, INC.")
    assert_that(results[0]["Country"]).is_equal_to("UNITED STATES (USA)")


def test_find_cars_by_mfr_id_955(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[0]["Mfr_ID"]).is_equal_to(955)
    print(results[0]["Mfr_Name"])


def test_find_cars_by_mfr_id_956(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[1]["Mfr_ID"]).is_equal_to(956)
    print(results[1]["Mfr_Name"])


def test_find_cars_by_mfr_id_957(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[2]["Mfr_ID"]).is_equal_to(957)
    print(results[2]["Mfr_Name"])


def test_find_cars_by_mfr_id_958(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[3]["Mfr_ID"]).is_equal_to(958)
    print(results[3]["Mfr_Name"])


def test_find_cars_by_mfr_id_959(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[4]["Mfr_ID"]).is_equal_to(959)
    print(results[4]["Mfr_Name"])


def test_find_cars_by_mfr_id_960(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[5]["Mfr_ID"]).is_equal_to(960)
    print(results[5]["Mfr_Name"])


def test_find_cars_by_mfr_id_961(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[6]["Mfr_ID"]).is_equal_to(961)
    print(results[6]["Mfr_Name"])


def test_find_cars_by_mfr_id_962(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[7]["Mfr_ID"]).is_equal_to(962)
    print(results[7]["Mfr_Name"])


def test_find_cars_by_mfr_id_964(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[8]["Mfr_ID"]).is_equal_to(964)
    print(results[8]["Mfr_Name"])


def test_find_cars_by_mfr_id_965(test_load_api):
    assert_that(test_load_api.status_code).is_equal_to(200)
    results = test_load_api.json()["Results"]
    assert_that(results[9]["Mfr_ID"]).is_equal_to(965)
    print(results[9]["Mfr_Name"])
