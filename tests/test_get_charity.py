import requests
from utils import api_helpers
from utils.config import CONFIG
from pages.login_page import LoginPage
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.parametrize('email, password', [(CONFIG['login_email'], CONFIG['login_password'])])
def test_get_pending_charity(browser,email,password):
    browser.get(CONFIG['base_url'])
    login_page = LoginPage(browser)
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login()
    WebDriverWait(browser, timeout=10).until(
        EC.url_contains('https://dashboard.dev.piiink.org/dashboard')
    )
    token = browser.execute_script("return window.localStorage.getItem('authToken');")
    header = {
        'Authorization' : f"Bearer {token}"
    }
    response = api_helpers.get_all_charity(header)
    data = response.json()
    assert response.status_code == 200
    assert 'data' in data


