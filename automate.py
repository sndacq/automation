from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

geckodriver = '/path/to/geckodriver.exe'
binary = '/path/to/firefox.exe'
address = 'http://192.168.254.254/'

username = ''
password = ''

options = Options()
options.headless = True
options.binary = binary

browser = webdriver.Firefox(options=options, executable_path=geckodriver)

try:
    browser.get(address)
    login = browser.find_element_by_id('logout_span')

    if login.text == 'Log In':
        print('Loggin in...')
        login.click()
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('pop_login').click()
        print('Successfully logged in')

        browser.get(f'{address}html/reboot.html')
        browser.find_element_by_id('undefined').click()
        browser.find_element_by_id('pop_confirm').click()
        time.sleep(5)
        print('Rebooting...')

except Exception as e:
    print(e)    

print('Exit Script')
browser.quit()
