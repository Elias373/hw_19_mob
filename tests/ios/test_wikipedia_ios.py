import allure
from selene import browser, have


@allure.title("Simple iOS test")
def test_ios_app_launch():
    browser.open('https://wikipedia.org')

    with allure.step('Check page loaded'):
        browser.element('.central-textlogo').should(have.text('Wikipedia'))
