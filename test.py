from playwright.sync_api import sync_playwright
from models.automationPratice import AutomationPratice
from pytest import fixture
from playwright.sync_api import sync_playwright

from models.basePage import BasePage

@fixture
def get_play():
    with sync_playwright() as play:
        yield play


@fixture
def setup(get_play):
    login = AutomationPratice(BasePage(get_play))
    return login
    


def test_case_aut(setup):
    setup.go_url()
    setup.click_button_sign()
    setup.type_username_and_password()
    setup.click_button_sign_acess()
    assert "My personal information" == setup.text_after_login() 
    setup.closeBrowser()