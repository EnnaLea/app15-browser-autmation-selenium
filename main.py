from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get("https://demoqa.com/login")

# Locate username, password and login button
username_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName' )))
password_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password' )))
login_button = driver.find_element(By.ID, 'login')


# Fill in username and password and click the button
username_filed.send_keys('pythondeveloper')
password_filed.send_keys('Pythondeveloper55#')
driver.execute_script("arguments[0].click();", login_button)


# Locate elements dropdown and textbox
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/span/div' )))
elements.click()

text_box= driver.find_element(By.ID, 'item-0')
driver.execute_script("arguments[0].click();", text_box)

# Locate form fields and submit button
full_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')


# Filling the form fields
full_name_field.send_keys('John Smith')
email_field.send_keys('smith@gmail.com')
current_address_field.send_keys('John Street 100, New York, USA')
permanent_address_field.send_keys('John Street 100, New York, USA')
driver.execute_script("arguments[0].click();", submit_button)


# Locate the upload and download section and the download button
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7' )))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)


input("Press Enter to close the browser")
driver.quit()