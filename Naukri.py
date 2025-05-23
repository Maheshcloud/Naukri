from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
# SModules required - selenium, webdriver_manager
# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

username = "${{ secrets.USERNAME }}"
password = "${{ secrets.PASSWORD }}"


# Navigate to Naukri login page
driver.get("https://www.naukri.com/nlogin/login")

# Login to Naukri
username_field = driver.find_element("id", "usernameField")
password_field = driver.find_element("id", "passwordField")
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/div[3]/div/button[1]')
time.sleep(2)
username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()

driver.maximize_window()
time.sleep(2) # Wait for elements to load

driver.get("https://www.naukri.com/mnjuser/profile?id=&altresid")
time.sleep(2)
implicit_wait = 10
driver.implicitly_wait(implicit_wait)
# element = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[4]/div")
# element.click()
edit_link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/span/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/em')
edit_link.click()
time.sleep(2)

save_button = driver.find_element(By.XPATH, '//*[@id="saveBasicDetailsBtn"]')
save_button.click()
time.sleep(2)
# Close the driver
#driver.quit()
