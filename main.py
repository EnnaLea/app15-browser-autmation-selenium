from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
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


input("Press Enter to close the browser")
driver.quit()