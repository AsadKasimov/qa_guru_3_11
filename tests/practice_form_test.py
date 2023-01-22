import allure
from demoqa_tests.model.pages.data import user
from demoqa_tests.model.pages.practice_form import PracticePage
from demoqa_tests.utils import attach
from selene.support.shared import browser

def test_practice():
    with allure.step('определяет данные для заполнения'):
        john = PracticePage(user)
    with allure.step('Заполняет форму'):
        john.fill().submit()
    with allure.step('проверяет заполненные данные'):
        john.assert_fields()

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)