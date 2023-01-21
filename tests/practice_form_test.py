import allure
from demoqa_tests.model.pages.data import user
from demoqa_tests.model.pages.practice_form import PracticePage


def test_practice():
    with allure.step('определяет данные для заполнения'):
        john = PracticePage(user)
    with allure.step('Заполняет форму'):
        john.fill().submit()
    with allure.step('проверяет заполненные данные'):
        john.assert_fields()