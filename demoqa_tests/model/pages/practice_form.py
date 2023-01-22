from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls.dropdown import JoeDrop
from demoqa_tests.model.controls.datepicker import JoeBirthday
from demoqa_tests.model.controls.radiobutton import JoeGender
from demoqa_tests.model.controls.checkbox import JoeHobby
from demoqa_tests.utils import path_to_file
from demoqa_tests.utils.scroll import scroll_to



class PracticePage:
    def __init__(self, person):
        self.person = person

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def fill(self):

        browser.open('/automation-practice-form')
        browser.element('#firstName').type(self.person.first_name)

        browser.element('#lastName').type(self.person.last_name)

        browser.element('#userEmail').type(self.person.email)
        male = JoeGender('[name=gender]', self.person.male)
        male.gender()
        browser.element('#userNumber').type(self.person.number)

        browser.element('#dateOfBirthInput').click()

        browser.element('.react-datepicker__month-select').click()
        month = JoeBirthday('.react-datepicker__month-select', self.person.month)
        month.date()

        browser.element('.react-datepicker__year-select').click()
        year = JoeBirthday('.react-datepicker__year-select', self.person.year)
        year.date()

        browser.element(f'.react-datepicker__day--0{self.person.day}').click()

        browser.element('#subjectsInput').type(self.person.subject).press_enter()

        happy = JoeHobby('[for^=hobbies-checkbox]', self.person.hobbies)
        happy.hobby()

        scroll_to('#currentAddress')

        browser.element('#currentAddress').type(self.person.address)

        path_to_file.create_path('#uploadPicture', self.person.picture)

        state = JoeDrop('#state', self.person.state)
        state.select()

        city = JoeDrop('#city', self.person.city)
        city.select()
        return self

    def assert_fields(self):
        browser.element('.table').all('td').even.should(have.texts(
            self.person.first_name + ' ' + self.person.last_name,
            self.person.email,
            self.person.male,
            self.person.number,
            self.person.assert_data,
            self.person.subject,
            self.person.hobbies,
            self.person.assert_picture,
            self.person.address,
            self.person.state + ' ' + self.person.city,

        ))
        return self
