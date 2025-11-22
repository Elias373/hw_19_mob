import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
import allure
import allure_commons
import dotenv

dotenv.load_dotenv()
user_name = os.getenv('BROWSERSTACK_USERNAME')
accesskey = os.getenv('BROWSERSTACK_ACCESS_KEY')


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="android",
                     help="Platform to run tests on: android or ios")


@pytest.fixture(scope='function')
def mobile_management(request):
    platform = request.config.getoption("--platform")

    if platform == "android":
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "platformVersion": "12.0",
            "deviceName": "Samsung Galaxy S22",
            "app": "bs://sample.app",  # Демо приложение Android
            'bstack:options': {
                "projectName": "Android App tests",
                "buildName": "browserstack-android-app",
                "userName": user_name,
                "accessKey": accesskey
            }
        })

    elif platform == "ios":
        options = XCUITestOptions().load_capabilities({
            "platformName": "ios",
            "platformVersion": "16",
            "deviceName": "iPhone 14",
            "app": "bs://sample.app",  # Демо приложение iOS
            'bstack:options': {
                "projectName": "IOS App tests",
                "buildName": "browserstack-ios-app",
                "userName": user_name,
                "accessKey": accesskey
            }
        })

    browser.config.timeout = 10.0

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    with allure.step('tear down app session'):
        browser.quit()