from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def post_on_facebook(caption, image_path):
    config = load_config()
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    
    # Log in
    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("pass")
    email.send_keys(config['facebook']['email'])
    password.send_keys(config['facebook']['password'])
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to post creation
    driver.find_element_by_xpath("//textarea[@name='xhpc_message']").click()
    time.sleep(2)

    # Add caption and upload image
    caption_field = driver.find_element_by_xpath("//textarea[@name='xhpc_message']")
    caption_field.send_keys(caption)
    upload_input = driver.find_element_by_xpath("//input[@type='file']")
    upload_input.send_keys(image_path)
    time.sleep(2)

    # Post
    driver.find_element_by_xpath("//button[contains(text(), 'Post')]").click()
    
    time.sleep(5)
    driver.quit()
