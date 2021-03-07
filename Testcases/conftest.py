from selenium import webdriver
import pytest
@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver


def pytest_configure(config):
    config._metadata['Project Name'] = 'orange HRM'
    config._metadata['Module name'] = 'Customer'
    config._metadata['Testsre name'] = 'Vishnu'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    metadata.pop("Packages",None)

