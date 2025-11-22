import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.utils.config import settings
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
            'browserName': 'chrome',
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
            'browserName': 'safari',
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

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    # СНИМОК ЭКРАНА - оставляем как PNG
    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    # ИСПРАВЛЕНИЕ: меняем XML на HTML для page_source
    allure.attach(
        browser.driver.page_source,
        name='page_source',
        attachment_type=allure.attachment_type.HTML,  # ← ИЗМЕНИТЬ ЗДЕСЬ
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()
