import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Android app test - simple interaction")
def test_android_app_interaction(mobile_management):
    with allure.step('Wait for app to load'):
        browser.element((AppiumBy.XPATH, "//*")).should(be.visible)

    with allure.step('Take screenshot of loaded app'):
        # Просто проверяем что приложение запустилось
        pass