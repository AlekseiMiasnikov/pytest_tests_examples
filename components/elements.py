from selene.support.shared.jquery_style import s
from allure import step


class Elements:
    @step('Работа с элементом - {selector}')
    def element(self, selector):
        return s(selector)
