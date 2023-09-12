from selenium import webdriver
from selenium.webdriver.common.by import By


    # Create a new instance of the Chrome web driver
driver = webdriver.Chrome()

    # Navigate to the login page
driver.get("http://127.0.0.1:5500/index.html")
    # Enter the email and password
email_element = driver.find_element(By.NAME,"username")
email_element.send_keys("test@example.com")

password_element = driver.find_element(By.NAME,"password")
password_element.send_keys("password")

    # Click the login button
login_button = driver.find_element(By.TAG_NAME,"input")
login_button.click()
driver.get("http://www.google.com")

    
