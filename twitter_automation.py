from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

def post_on_twitter(caption, image_path):
    config = load_config()
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")
    
    # Log in
    username = driver.find_element_by_name("session[username_or_email]")
    password = driver.find_element_by_name("session[password]")
    username.send_keys(config['twitter']['username'])
    password.send_keys(config['twitter']['password'])
    password.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to tweet creation
    driver.find_element_by_xpath("//a[@aria-label='Tweet']").click()
    time.sleep(2)
    
    # Upload the image
    driver.find_element_by_xpath("//input[@type='file']").send_keys(image_path)
    time.sleep(2)

    # Add caption and post
    caption_field = driver.find_element_by_xpath("//div[@aria-label='Tweet text']")
    caption_field.send_keys(caption)
    driver.find_element_by_xpath("//div[@data-testid='tweetButtonInline']").click()
    
    time.sleep(5)
    driver.quit()
