from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import sys

# webdriver manager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # Instantiate the browser here
    
    username = "Your LambdaTest Username"
    accessToken = "Your LambdaTest Access Token"
    
    gridUrl = "hub.lambdatest.com/wd/hub"
   
    capabilities = {
        'LT:Options' : {
            "user" : "Your LambdaTest Username",
            "accessKey" : "Your LambdaTest Access Key",
            "build" : "your build name",
            "name" : "your test name",
            "platformName" : "Windows 11",
        },
        "browserName" : "Chrome",
        "browserVersion" : "103.0",
    }

    url = "https://"+username+":"+accessToken+"@"+gridUrl
    
    browser = webdriver.Remote(
        command_executor=url,
        desired_capabilities=capabilities
    )

    browser.maximize_window()

    yield browser
    
    # Close the browser after the test is finished
    browser.quit

# It will be run
def test_01(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud"

#It will be skipped 
@pytest.mark.skip
def test_02(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud"

#It will be skipped if run on linux
@pytest.mark.skipif(sys.platform.startswith("linux"), reason="Not available on Linux")
def test_03(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud"

#It will be skipped if run on windows
@pytest.mark.skipif(sys.platform.startswith("win"), reason="Not available on Windows")
def test_04(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud"

#It will be skipped when running pytest -k "not 05" in command line
def test_05(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud" 

#It will be skipped when adding an addopts option in pytest.ini file -k "not 06"
def test_06(browser):
    browser.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    assert browser.title == "Selenium Grid Online | Run Selenium Test On Cloud" 