from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def post_on_linkedin(caption, image_path):
    config = load_config()
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/")
    
    # Log in
    username = driver.find_element_by_name("session_key")
    password = driver.find_element_by_name("session_password")
    username.send_keys(config['linkedin']['username'])
    password.send_keys(config['linkedin']['password'])
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to post creation
    driver.find_element_by_xpath("//button[contains(text(), 'Start a post')]").click()
    time.sleep(2)
    
    # Upload the image
    driver.find_element_by_xpath("//input[@type='file']").send_keys(image_path)
    time.sleep(2)

    # Add caption and post
    caption_field = driver.find_element_by_xpath("//div[@role='textbox']")
    caption_field.send_keys(caption)
    driver.find_element_by_xpath("//button[contains(text(), 'Post')]").click()
    
    time.sleep(5)
    driver.quit()
