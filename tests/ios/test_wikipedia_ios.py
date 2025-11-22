import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("iOS app test - simple interaction")
def test_ios_app_interaction(mobile_management):
    with allure.step('Wait for app to load'):
        browser.element((AppiumBy.XPATH, "//*")).should(be.visible)

    with allure.step('Take screenshot of loaded app'):
        # Просто проверяем что приложение запустилось
        pass