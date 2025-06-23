import pytest
from utils.config import CONFIG
from pages.login_page import LoginPage


@pytest.mark.parametrize('email, password', [(CONFIG['login_email'], CONFIG['login_password'])])
def test_login(browser, email, password):
    browser.get(CONFIG['base_url'])
    login_page = LoginPage(browser)
    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login()
    assert 'Piiink Admin Panel' == browser.title


