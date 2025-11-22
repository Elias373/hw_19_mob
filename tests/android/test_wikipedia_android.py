import allure
from selene import browser, have


@allure.title("Simple Android test")
def test_search():
    browser.open('https://wikipedia.org')

    with allure.step('Type search'):
        browser.element('#searchInput').type('Appium')
        browser.element('.pure-button').click()

    with allure.step('Verify content found'):
        browser.element('#firstHeading').should(have.text('Appium'))