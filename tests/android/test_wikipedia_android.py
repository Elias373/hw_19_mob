import allure
from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Open article in Wikipedia app")
def test_open_wikipedia_article():
    with allure.step("Click search"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Type search"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Python")

    with allure.step("Click article"):
        browser.element((AppiumBy.XPATH, "//*[@text='Python (programming language)']")).click()