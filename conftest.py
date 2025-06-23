from selenium import webdriver

import pytest

@pytest.fixture
def browser():
    print('Setting up the browser....')
    options = webdriver.ChromeOptions()
    options.add_argument('--Headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    print('Tearing down the browser....')
    driver.quit()

    