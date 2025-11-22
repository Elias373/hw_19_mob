import os
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser, support
import allure
import allure_commons
from src.utils.config import settings


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android",
                     help="Platform to run tests on: android or ios")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    platform = request.config.getoption("--platform")

    if platform == "android":
        options = UiAutomator2Options().load_capabilities({
            'platformName': 'android',
            'app': settings.android_app,
            'bstack:options': {
                'userName': settings.browserstack_username,
                'accessKey': settings.browserstack_access_key,
                'deviceName': settings.android_device,
                'platformVersion': settings.android_platform_version,
                'projectName': 'Android Wikipedia',
                'buildName': 'android-wikipedia',
                'sessionName': 'Wikipedia test',
            }
        })

    elif platform == "ios":
        options = XCUITestOptions().load_capabilities({
            'platformName': 'ios',
            'app': settings.ios_app,
            'bstack:options': {
                'userName': settings.browserstack_username,
                'accessKey': settings.browserstack_access_key,
                'deviceName': settings.ios_device,
                'platformVersion': settings.ios_platform_version,
                'projectName': 'iOS Wikipedia',
                'buildName': 'ios-wikipedia',
                'sessionName': 'Wikipedia test',
            }
        })

    with allure.step('Start session'):
        browser.config.driver = webdriver.Remote(
            f"https://{settings.browserstack_url}",
            options=options
        )

    browser.config.timeout = 10.0
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    with allure.step('Close session'):
        browser.quit()