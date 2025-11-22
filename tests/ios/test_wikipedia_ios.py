import allure
from selene import browser, be, have


@allure.title("Simple iOS browser test")
def test_simple_ios():
    with allure.step('Open website and verify'):
        browser.open('https://example.com')
        browser.element('h1').should(have.text('Example Domain'))

    with allure.step('Perform interaction'):
        # Просто проверяем что можем взаимодействовать с элементами
        browser.element('a').should(be.visible)

    with allure.step('Verify iOS platform'):
        # Проверяем что тест запущен на iOS
        capabilities = browser.driver.capabilities
        platform = capabilities.get('platformName', '').lower()
        assert platform == 'ios'
        print(f"Test running on: {platform}")