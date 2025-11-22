import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title("iOS app interaction test")
def test_ios(mobile_management):  # ← ИЗМЕНИЛ macos_management на mobile_management
    text_to_input = 'Hello,world!'

    with allure.step("Click on Text Button"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()

    with allure.step(f"Type text: {text_to_input}"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys(
            text_to_input + "\n")

    with allure.step("Verify text output"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(
            have.exact_text(text_to_input)
        )