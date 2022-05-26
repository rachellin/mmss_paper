from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()

driver.get('https://twitter.com')

def login (username, password):
    # enter username
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    username_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    username_field.click()
    username_field.send_keys(username)

    # enter password
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    password_field = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    password_field.click()
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN) # enter to login
