from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from dates import date_ranges

import time

driver = webdriver.Chrome("chromedriver.exe")
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

# TODO: don't need to login to get tweets!!!

#driver.get('https://twitter.com/search?q=thinspo')

# 1. count tweets by time 


# TESTING
driver.get('https://twitter.com/search?q=thinspo%20until%3A2015-01-02%20since%3A2015-01-01&src=typed_query')
count = 0
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[6]/div/div/div/article/div/div/div/div[2]')))
# post = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[6]/div/div/div/article/div/div/div/div[2]')
# post.click()

# timeline container:
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div

tl_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div'
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, tl_xpath)))
parent_div = driver.find_element_by_xpath(tl_xpath)
count_of_divs = len(parent_div.find_elements_by_xpath("./div"))
print(count_of_divs)

time.sleep(1)
body = driver.find_elements_by_tag_name('body')
for _ in range(100):
   body.send.keys(Keys.PAGE_DONW)
   time.sleep(0.2)
tweets = driver.find_elements_by_class_name('tweet-text')
for tweet in tweets:
    print(tweet.text)