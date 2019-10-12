from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait
from config import *
from time import sleep

import sys


def login(browser):
    login = browser.find_element_by_id('logout_span')

    if login.text == 'Log In':
        print('Loggin in...')
        login.click()
        WebDriverWait(browser, 3).until(
            ec.presence_of_element_located((By.ID, 'username')))
        browser.find_element_by_id('username').send_keys(username)
        browser.find_element_by_id('password').send_keys(password)
        browser.find_element_by_id('pop_login').click()
        print('Successfully logged in')

def filter_mac(browser, disable=False):
    # TODO: Validate filter before resetting
    browser.get(f'{address}html/wlanmacfilter.html')
    select = Select(browser.find_element_by_id('ssid_select_service'))
    if disable:
        select.select_by_value('0')
    else:
        select.select_by_value('1')
        for idx, val in enumerate(allowed_mac):
            element_id = f'ssid_input_WifiMacFilterMac{idx}'
            browser.find_element_by_id(element_id).send_keys(val)
    wait_then_click(browser, 'apply')
    wait_then_click(browser, 'pop_confirm')

def reboot(browser):
    browser.get(f'{address}html/reboot.html')
    wait_then_click(browser, 'undefined')
    wait_then_click(browser, 'pop_confirm')
    print('Rebooting...')    

def wait_then_click(browser, id):
        WebDriverWait(browser, 3).until(
            ec.presence_of_element_located((By.ID, id)))
        browser.find_element_by_id(id).click()
        sleep(3)

def main(args):
    options = Options()
    options.headless = True
    options.binary = binary

    browser = webdriver.Firefox(options=options, executable_path=geckodriver)

    try:
        browser.get(address)
        login(browser)
        if args == '1':
            reboot(browser)
        elif args == '2':
            filter_mac(browser)
        elif args == '3':
            filter_mac(browser, True)
        else:
            print('Invalid argument: Use [1] to reboot, [2] to filter and [3] to reset')

    except Exception as e:
        print(e)

    finally:
        print('Exit Script')
        browser.quit()


if __name__ == '__main__':
    main(sys.argv[1])
