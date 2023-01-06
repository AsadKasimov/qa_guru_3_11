from selene import have
from selene.support.shared import browser

class JoeBirthday:
    def __init__(self,selector, value):
        self.selector = selector
        self.value = value
    def date(self):
        browser.element(self.selector).all('option').element_by(have.exact_text(self.value)).click()