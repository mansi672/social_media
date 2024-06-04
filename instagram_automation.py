from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def post_on_instagram(caption, image_path):
    config = load_config()
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    
    # Log in
    username = driver.find_element_by_name("mansisharma2579")
    password = driver.find_element_by_name("MANSIWEDSGAURAV")
    username.send_keys(config['instagram']['mansisharma2579'])
    password.send_keys(config['instagram']['MANSIWEDSGAURAV'])
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to post upload
    driver.find_element_by_xpath("//div[contains(text(), 'Create')]").click()
    time.sleep(2)
    
    # Upload the image
    upload_input = driver.find_element_by_xpath("//input[@type='file']")
    upload_input.send_keys(image_path)
    time.sleep(2)

    # Add caption and post
    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
    caption_field.send_keys(caption)
    driver.find_element_by_xpath("//button[contains(text(), 'Share')]").click()
    
    time.sleep(5)
    driver.quit()
