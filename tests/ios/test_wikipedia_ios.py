import allure
from selene import browser, have
import time


@allure.title("Simple Android test")
def test_search():
    browser.open('https://wikipedia.org')

    with allure.step('Type search'):
        browser.element('#searchInput').type('Appium')


        time.sleep(2)


        search_button = browser.driver.find_element_by_css_selector('.pure-button')
        browser.driver.execute_script("arguments[0].click();", search_button)

    with allure.step('Verify content found'):
        browser.element('#firstHeading').should(have.text('Appium'))
