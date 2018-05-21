import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class HomePageTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument('-headless')
        self.browser = Firefox(executable_path=r'C:\Users\yurblago\Documents\tdd-intro\geckodriver\geckodriver.exe',
                               options=options,
                               firefox_binary=r"C:\Users\yurblago\AppData\Local\Mozilla Firefox\firefox.exe"
                               )

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # Edith hears about a cool to-do lists site
        self.browser.get('http:localhost:8000')

        # She sees the title and header mention to-do lists
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('To-Do', header.text)

        # She is invited to enter a to-do item straight away
        self.fail('Finish this test')

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main()
