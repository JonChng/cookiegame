from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = "/Users/jonathanchng/Downloads/chromedriver_mac64/chromedriver"
url = "https://orteil.dashnet.org/cookieclicker/"


driver = webdriver.Chrome(chromedriver_path)

driver.get(url)

driver.implicitly_wait(20)

english = driver.find_element(By.XPATH,"//*[@id='langSelect-EN']")
english.click()



timeout = time.time() + 5

driver.implicitly_wait(10)
ok = True
while ok:

    element = driver.find_element(By.ID, "bigCookie")
    element.click()

    if time.time() >= timeout:
        prices1 = []
        #Get Cookie Number
        cookies = driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0]

        try:
            cookies = int(cookies)

        except ValueError:
            cookie = cookies.split(",")
            cookies = int("".join(i for i in cookie))

        print(cookies)
        purchases = driver.find_element(By.ID, 'products')

        to_buy = purchases.find_elements(By.CLASS_NAME, "product")

        for i in to_buy[::-1]:
            price = i.find_element(By.CLASS_NAME, "price").text
            if price == "":
                continue

            try:
                price = float(price)
                print(price)

            except ValueError:
                if 'm' in list(price):
                    price = price.split()[0] * 1000000
                    price = float(price)
                else:
                    prices = price.split(",")
                    print(prices)
                    price = "".join(i for i in prices)
                    print(price)
                    price = float(price)
                    print(type(price))

            if cookies >= price:
                i.click()



        # print(possible_buys)
        # for i in possible_buys:
        #     price = i.find_element(By.CLASS_NAME, "price")
        #     print(price.text)

        timeout = time.time() + 5
#


#


driver.quit()