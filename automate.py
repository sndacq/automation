from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from config import *
from time import sleep


def login(browser):
    login = browser.find_element_by_id('logout_span')

    if login.text == 'Log In':
        print('Loggin in...')
        login.click()
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('pop_login').click()
        print('Successfully logged in')

def filter_mac(browser):
    browser.get(f'{address}html/wlanmacfilter.html')
    select = Select(browser.find_element_by_id('ssid_select_service'))
    select.select_by_value('1')
    for idx, val in enumerate(allowed_mac):
        element_id = f'ssid_input_WifiMacFilterMac{idx}'
        browser.find_element_by_id(element_id).send_keys(val)
    browser.find_element_by_id('apply').click()
    sleep(3)
    browser.find_element_by_id('pop_confirm').click()
    sleep(3)


def reboot(browser):
    browser.get(f'{address}html/reboot.html')
    browser.find_element_by_id('undefined').click()
    # TODO: add dynamic waiting for elements
    sleep(3)
    browser.find_element_by_id('pop_confirm').click()
    sleep(3)
    print('Rebooting...')    

def main():
    options = Options()
    options.headless = True
    options.binary = binary

    browser = webdriver.Firefox(options=options, executable_path=geckodriver)

    try:
        browser.get(address)
        login(browser)
        reboot(browser)

    except Exception as e:
        print(e)    

    print('Exit Script')
    browser.quit()


if __name__ == '__main__':
    main()

