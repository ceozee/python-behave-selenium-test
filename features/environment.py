from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
from datetime import datetime
from os import path, makedirs


def before_all(context):
    #Get config in behave.ini
    config = ConfigParser()
    config.read('behave.ini')
    browser = config._sections['profile']['browser']
    env = config._sections['profile']['env']
    context.config_browser = config._sections[browser]
    context.config_env = config._sections[env]

    #browser used
    def browser_selector(exec_path):
        if context.config_browser['profile'] == 'firefox':
            context.driver = webdriver.Firefox(executable_path=exec_path)
        elif context.config_browser['profile'] == 'edge':
            context.driver = webdriver.Edge(executable_path=exec_path)
        elif context.config_browser['profile'] == 'chrome':
            context.driver = webdriver.Chrome(executable_path=exec_path)
        else:
            print('browser not defined')

    #Browser/driver initiated
    browser_selector(context.config_browser['browser_executable_path'])
    context.driver.implicitly_wait(2)

    #URL initiated
    context.url = context.config_env['url']

    #screenshot folder creation
    folder_exists = path.exists('screenshots')
    if folder_exists is False:
        makedirs('./screenshots')


def after_step(context, step):
    if step.status == 'failed':
        timestamp = datetime.now()
        screenshot_name = str(int(timestamp.strftime('%Y%m%d%H%M%S')))
        context.driver.save_screenshot(f'screenshots/{screenshot_name}_error.png')

def after_all(context):
    context.driver.close()
    context.driver.quit()