import datetime


class Base():
    def __init__(self, browser):
        self.browser = browser

    def get_current_url(self):
        get_url = self.browser.current_url
        print('Current URL:' + get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S.')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.browser.save_screenshot('C:\\Users\\User\\PycharmProjects\\pythonProject\\screen\\' + name_screenshot)
