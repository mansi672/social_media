from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def post_on_pinterest(caption, image_path):
    config = load_config()
    driver = webdriver.Chrome()
    driver.get("https://www.pinterest.com/login/")
    
    # Log in
    username = driver.find_element_by_name("id")
    password = driver.find_element_by_name("password")
    username.send_keys(config['pinterest']['username'])
    password.send_keys(config['pinterest']['password'])
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to pin creation
    driver.find_element_by_xpath("//div[@data-test-id='header-create-menu-button']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@data-test-id='header-create-pin']").click()
    time.sleep(2)
    
    # Upload the image
    driver.find_element_by_xpath("//input[@type='file']").send_keys(image_path)
    time.sleep(2)

    # Add caption and post
    caption_field = driver.find_element_by_xpath("//textarea[@placeholder='Tell everyone what your Pin is about...']")
    caption_field.send_keys(caption)
    driver.find_element_by_xpath("//button[contains(text(), 'Save')]").click()
    
    time.sleep(5)
    driver.quit()
