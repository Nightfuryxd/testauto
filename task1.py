from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the web driver (e.g., Chrome)
driver = webdriver.Chrome()  # or specify the path to chromedriver
driver.maximize_window()

try:
    # Navigate to the website
    driver.get('https://practicetestautomation.com/practice-test-login/')

    # Find and fill the username field
    username_field = driver.find_element(By.ID, 'username')  # adjust the selector as needed
    username_field.send_keys('student')
    
    # Wait for the page to load
    time.sleep(2)

    # Find and fill the password field
    password_field = driver.find_element(By.ID, 'password')  # adjust the selector as needed
    password_field.send_keys('Password123')

    time.sleep(3)


    # Submit the login form
    login_button = driver.find_element(By.ID, 'submit')  # adjust the selector as needed
    login_button.click()

    # Wait for login to complete
    time.sleep(5)  

    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
            
    logout_button.click()

    # Wait for logout to complete
    time.sleep(3)

 
finally:
    # Close the browser
    driver.quit()
