from selenium import webdriver
from web.web import Web


def get_web(browser):
    if browser == "chrome":
        return Web(webdriver.Chrome('web/drivers/chromedriver'))
    if browser == "firefox":
        return Web(webdriver.Firefox('web/drivers/geckodriver'))
