import allure
from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Open article in Wikipedia iOS app")
def test_open_wikipedia_article_ios():
    with allure.step("Click search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Type search"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTextField[@name='Search Wikipedia']")).type("Python")

    with allure.step("Click article"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Python (programming language)']")).click()