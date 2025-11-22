import allure
from selene import browser, be


@allure.title("Simple iOS browser test")
def test_simple_ios():
    with allure.step('Open website'):
        browser.open('https://example.com')

    with allure.step('Verify page loaded'):
        # Просто проверяем что страница загрузилась
        browser.element('h1').should(be.visible)

    with allure.step('Verify iOS platform'):
        # Проверяем что тест запущен на iOS
        capabilities = browser.driver.capabilities
        platform = capabilities.get('platformName', '').lower()
        assert platform == 'ios'