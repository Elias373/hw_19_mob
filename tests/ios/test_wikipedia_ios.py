import allure
import pytest
from selene import browser


@allure.title("Simple iOS test")
def test_ios_app_launch():

    with allure.step('Check iOS app is running'):
        assert browser.driver is not None
        assert browser.driver.session_id is not None

    with allure.step('Verify we can interact with app'):
        capabilities = browser.driver.capabilities
        platform = capabilities.get('platformName', '').lower()
        assert platform == 'ios', f"Expected iOS, but got {platform}"
