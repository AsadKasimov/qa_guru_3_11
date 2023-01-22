import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.window_width = 1400
    browser.config.window_height = 800
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()