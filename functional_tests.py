from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

if __name__ == '__main__':
    options = Options()
    options.add_argument('-headless')
    browser = Firefox(executable_path=r'C:\Users\yurblago\Documents\tdd-intro\geckodriver\geckodriver.exe',
                      firefox_options=options,
                      firefox_binary=r"C:\Users\yurblago\AppData\Local\Mozilla Firefox\firefox.exe"
                      )
    browser.get('http:localhost:8000')
    assert 'Django' in browser.title
