from selene import have

from components.elements import Elements
from allure import step

from components.selectors import H2


class BasePage(Elements):
    def __init__(self, driver):
        self.driver = driver

    @step('Открытие страницы с адресом - {url}')
    def open(self, url='/'):
        self.driver.open(url)

    @step('Проверка заголовка - {title}')
    def check_title(self, title):
        self.element(H2).should(have.text(title))

    @step('Клик по кнопке')
    def click_button(self, element):
        self.element(element).click()
