import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy


@allure.title("Search test on Android")
def test_search_on_android():
    with allure.step('Search for Appium'):

        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()


        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')


        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

    with allure.step('Verify we tried to open article'):

        assert browser.driver.current_activity is not None