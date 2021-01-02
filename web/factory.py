from selenium import webdriver
from webdriver_manager.firefox import FirefoxDriverManager
from web.web import Web


def get_web(browser):
    if browser == "chrome":
        #return Web(webdriver.Chrome(ChromeDriverManager().install()))
        return Web(webdriver.Chrome('web/drivers/chromedriver'))
    if browser == "firefox":
        return Web(webdriver.Firefox(FirefoxDriverManager().install()))
