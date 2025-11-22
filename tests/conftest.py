import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver
from selene import browser
import allure
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
                'projectName': 'Android Tests',
                'buildName': 'android-build-1',
                'sessionName': 'Android Wikipedia Test',
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
                'projectName': 'iOS Tests',
                'buildName': 'ios-build-1',
                'sessionName': 'iOS Wikipedia Test',
            }
        })

    else:
        raise ValueError(f"Unsupported platform: {platform}")

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            f"https://{settings.browserstack_url}",
            options=options
        )

    yield

    with allure.step('tear down app session'):
        browser.quit()