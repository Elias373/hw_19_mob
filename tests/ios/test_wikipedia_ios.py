import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Search test on iOS")
def test_search_on_ios():
    with allure.step('Search for Python'):

        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()


        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('Python')


        browser.element((AppiumBy.ACCESSIBILITY_ID, "Return")).click()

    with allure.step('Verify interaction was performed'):

        text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
        text_output.should(be.visible)