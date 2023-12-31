#from selenium import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching firefox browser")
    else:
        driver = webdriver.Chrome()

    return driver

def pytest_addoption(parser): # This will get  the value from CLI hooks
    parser.addoption('--browser' , action='store')

@pytest.fixture()
def browser(request): # this will return the browser value to set up method
    return request.config.getoption('--browser')

############# Pytest HTML Report ################

# It is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata = {
        "Project Name" : 'nop Commerce',
        'Module Name' : 'Customers',
        'Tester' : 'Preeti',
    }
# It is hook for delete/modify environment info to html report
@pytest.mark.optionalHook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
