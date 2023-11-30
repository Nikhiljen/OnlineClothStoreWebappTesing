import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def Setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    try:
        if browser_name == "chrome":
            path = r"C:\driver\chromedriver-win64\chromedriver.exe"
            service = ChromeService(executable_path=path)
            driver = webdriver.Chrome(service=service)
        elif browser_name == "msedge":
            path = r"C:\driver\msedgedriver.exe"
            service = ChromeService(executable_path=path)
            driver = webdriver.Chrome(service=service)

    except TimeoutException:
        print("Timed out waiting for page to load.")

    driver.get("http://automationexercise.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

