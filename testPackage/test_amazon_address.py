import time
from faker import Faker
import random

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='/home/shashi/PycharmProjects/pythonSelenium/resource/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()



def test_amazon_address():
    driver.get("https://www.amazon.in/")
    assert driver.title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
    assert driver.current_url == "https://www.amazon.in/"


def test_validate_login():
    driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
    driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys("9110164834")
    driver.find_element(By.XPATH,"//input[@id='continue']").click()
    driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys("Shashi@123")
    driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
    text= driver.find_element(By.XPATH,"//span[@id='nav-link-accountList-nav-line-1']").text
    print(text)
    assert text.lower().__contains__("shashi")

def test_adding_new_address():
    driver.find_element(By.XPATH, '//a[@id=\'nav-global-location-popover-link\']').click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[normalize-space()='Add an address or pick-up point']").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='a-box first-desktop-address-tile']").click()
    time.sleep(5)
    fake = Faker('en_IN')  # Specify Indian locale
    list = [845305, 110001, 530068, 600001, 211001, 400001, 147301, 826124]
    first_digit = fake.random_element(elements=('1', '2', '3', '4', '5', '6', '7', '8', '9'))
    remaining_digits = fake.random_number(digits=9)
    phone_number = f"{first_digit}{remaining_digits}"
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-enterAddressFullName']").send_keys(fake.name())
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-enterAddressPhoneNumber']").send_keys(phone_number)
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-enterAddressPostalCode']").send_keys(random.choice(list))

    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']").send_keys(fake.address())

    driver.find_element(By.XPATH,"//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']").click()
    time.sleep(20)
    try:
        review = driver.find_element(By.XPATH, "//h4[normalize-space()='Review your address']")
        if review.is_displayed():
            driver.find_element(By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']").click()

    except NoSuchElementException:
        print("exception ")


