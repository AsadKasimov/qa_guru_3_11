from demoqa_tests.model.pages.data import user
from demoqa_tests.model.pages.practice_form import PracticePage


def test_practice():
    john = PracticePage(user)
    john.fill().submit()
    john.assert_fields()

