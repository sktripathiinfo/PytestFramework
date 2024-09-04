import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Adding command line hook
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif browser == "IE":
        driver = webdriver.Ie()
        driver.maximize_window()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver

    # The driver belongs to local driver - driver.get, driver.maximize
    # and cls.driver belongs to the test_end2end class driver

    yield
    driver.close()
