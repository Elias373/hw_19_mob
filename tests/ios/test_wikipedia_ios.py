import allure
from selene import browser, be, have


@allure.title("Simple iOS browser test")
def test_simple_ios():
    with allure.step('Open website'):
        browser.open('https://example.com')

    with allure.step('Verify page loaded'):
        # Просто проверяем что страница загрузилась
        browser.element('h1').should(have.text('Example Domain'))

    with allure.step('Perform click interaction'):
        # Выполняем клик на ссылке
        browser.element('a').click()

    with allure.step('Verify interaction completed'):
        # Проверяем что URL изменился после клика
        assert 'iana' in browser.driver.current_url.lower()