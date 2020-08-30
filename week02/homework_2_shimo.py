from logging import log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json


def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


def login_shimo(config):
    browser = webdriver.Chrome(executable_path=config['driver_path'])
    try:
        browser.get('https://shimo.im/login?from=home')
        WebDriverWait(browser, 10)
        input_email = browser.find_element_by_name('mobileOrEmail')
        input_email.send_keys(config['email'])
        input_pwd = browser.find_element_by_name('password')
        input_pwd.send_keys(config['pwd'])
        WebDriverWait(browser, 5)
        current_url = browser.current_url
        cookies=browser.get_cookies()
    finally:
        browser.close()
    return cookies, current_url


if __name__ == "__main__":
    config=load_config()
    cookies, current_url=login_shimo(config)
    print(cookies)
    print(current_url)
