from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver = r'C:\\Python37\\geckodriver.exe'
binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

username = ''
password = ''

options = Options()
# options.headless = True
options.binary = binary

browser = webdriver.Firefox(options=options, executable_path=geckodriver)
browser.get('http://192.168.254.254/')

login = browser.find_element_by_id('logout_span')
if login.text == 'Log In':
    login.click()
    browser.find_element_by_id('username').send_keys(username)
    browser.find_element_by_id ('password').send_keys(password)
    browser.find_element_by_id ('pop_login').click()






browser.quit()
