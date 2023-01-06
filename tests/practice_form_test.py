from demoqa_tests.model.pages.data import user
from demoqa_tests.model.pages.practice_form import PracticePage


def test_practice():
    john = PracticePage(user)
    john.given_opened()
    (john.type_firstname()
        .type_lastname()
        .type_email()
        .select_gender()
        .type_phone_number()
        .click_on_datepicker()
        .pick_month()
        .pick_year()
        .pick_day()
        .type_subject()
        .select_hobby()
        .scroll_to_address()
        .type_address()
        .upload_picture()
        .select_state()
        .select_city()
    )
    john.submit()
    john.assert_fields()
'''    
def test_student_registration_form():
    practice_form.given_opened()

    # WHEN
    practice_form.type_firstname('World')
    practice_form.type_lastname('Peace')
    practice_form.type_email('qwe@mail.com')

    practice_form.select_gender('Male')

    practice_form.type_phone_number('9998887755')

    practice_form.click_on_datepicker()
    practice_form.pick_month('May')
    practice_form.pick_year('1999')
    practice_form.pick_day(11)

    practice_form.type_subject('English')

    practice_form.select_hobby('Sports')

    practice_form.scroll_to_address()
    practice_form.type_address('Some address')

    practice_form.upload_picture('resources/image.PNG')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # THEN

    practice_form.assert_fields(
            'World Peace',
            'qwe@mail.com',
            'Male',
            '9998887755',
            '11 May,1999',
            'English',
            'Sports',
            'image.PNG',
            'Some address',
            'NCR Delhi'
    )
'''