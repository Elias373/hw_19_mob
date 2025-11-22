import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Android Wikipedia search test")
def test_android_wikipedia_search(mobile_management):
    with allure.step("Click search button"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Type search query"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step("Click on search result"):
        browser.element((AppiumBy.XPATH, "//*[@text='Python (programming language)']")).click()

    with allure.step("Verify article opened"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/page_contents_container")).should(be.visible)