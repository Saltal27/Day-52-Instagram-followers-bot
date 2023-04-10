import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# my Instagram dummy account credentials
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# driver path
chrome_driver_path = "C:\Development\chromedriver.exe"


class Instagram_followers_bot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(executable_path=chrome_driver_path)
        self.driver = WebDriver(service=service, options=options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)

        credentials = self.driver.find_elements(By.TAG_NAME, 'input')
        email = credentials[0]
        password = credentials[1]

        email.send_keys(MY_EMAIL)
        password.send_keys(MY_PASSWORD)
        password.send_keys(Keys.ENTER)

    def search_for_account(self, account_username):
        self.driver.get("https://www.instagram.com/{}/".format(account_username))
        time.sleep(10)

    def follow_followers(self):
        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, ' followers')
        followers.click()
        time.sleep(5)

        # scrolling down the followers list
        background = self.driver.find_element(By.CSS_SELECTOR, '._aano .x9f619')
        for _ in range(1000):
            background.send_keys(Keys.ARROW_DOWN)

        # following the followers
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '.x7r02ix .x9f619 ._acan')
        for button in follow_buttons:
            try:
                button.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, '.x1ja2u2z ._a9_1')
                cancel.click()

            time.sleep(0.1)


instagram_bot = Instagram_followers_bot()
instagram_bot.login()
time.sleep(15)
instagram_bot.search_for_account("smartphone_photography_101")
instagram_bot.follow_followers()
