from selene import have
from selene.support.shared import browser

class JoeDrop:
    def __init__(self,selector, by_te):
        self.selector = selector
        self.by_te = by_te
    def select(self):
        browser.element(self.selector).click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(self.by_te)
        ).click()
