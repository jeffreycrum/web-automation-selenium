import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebAutomation:
    TEST_URL = "https://demoqa.com/login"
    USER = "jec"
    PASS = "Testuser@1"

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-mac-arm64/chromedriver')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        self.driver.get(WebAutomation.TEST_URL)

        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, "login")

        username_field.send_keys(username)
        password_field.send_keys(password)

        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        element.click()

        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        curr_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        perm_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, "submit")

        fullname_field.send_keys("Joe Snow")
        email_field.send_keys("j_snow@yahoo.com")
        curr_address_field.send_keys("123 3rd St, Tampa, FL 33640")
        perm_address_field.send_keys("1234 4th St, Tampa, FL 33644")
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
        self.driver.execute_script("arguments[0].click();", upload_download)

        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()

    def run_all(self):
        auto = WebAutomation()
        auto.login(WebAutomation.USER, WebAutomation.PASS)
        auto.fill_form()
        auto.download()
        auto.close()


a = WebAutomation()
a.run_all()
