from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"
url = "https://orteil.dashnet.org/cookieclicker/"


driver = webdriver.Chrome(chromedriver_path)

driver.get(url)

driver.implicitly_wait(10)

english = driver.find_element(By.XPATH,"//*[@id='langSelect-EN']")
english.click()

ok = True
while ok:
    element = driver.find_element(By.ID,"bigCookie")
    element.click()


