import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class HomePageTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.browser = Firefox(executable_path=r'C:\Users\yurblago\Documents\tdd-intro\geckodriver\geckodriver.exe',
                               options=options,
                               firefox_binary=r"C:\Users\yurblago\AppData\Local\Mozilla Firefox\firefox.exe"
                               )

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http:localhost:8000')
        self.assertIn('To-Do', self.browser.title)


if __name__ == '__main__':
    unittest.main()
