from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


#Bread and butter for everything i need
"""driver.get("https://google.de")
time.sleep(3)

WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)

find_element = driver.find_element(By.ID, "W0wltc")
find_element.click()

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
time.sleep(1)
input_element.send_keys("Ac-130Beats" +Keys.ENTER)

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Ac-130Beats"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ac-130Beats")
link.click()
time.sleep(10)



input("Drücke Enter wenn du das Programm beenden möchtest")
driver.quit()"""

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)
accept = driver.find_element(By.CLASS_NAME,"fc-button-label")
accept.click()
language = driver.find_element(By.ID, "langSelect-DE")
language.click()
cookie = driver.find_element(By.ID,"bigCookie")

product_price_prefix = "productPrice"
product_prefix = "product"


while True:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    cookie.click()
    cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))


    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "" )

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break



"""Mi4wNTJ8fDE3MDMwODQ0MDY3MDU7MTcwMzA4NDQ
wNjcwNTsxNzAzMDkwMTU0NTM0O01jTmluamE7dGtraX
Q7MCwxLDAsMCwwLDAsMHwxMTExMTEwMTEwMDEwMTEw
MDEwMTAxMTAwMDF8MjYzNzE2MTguOTI3NTMzMDU7M
TM4NzYwMTE1LjkyNzQ1Mjk4OzE2NDI7NDsxMDg3MjQwLjk2M
DUwNDkyODs4OzA7MDswOzA7MDswOzA7MDswO
zQ7MDswOzA7ODswOzA7Y2hya
XN0bWFzOzA7MDswOzA7MDswOzA7LTE7LTE7L
TE7LTE7LTE7MDswOzA7MDs3NTswOzA7LTE7LTE
7MTcwMzA4NDQwNjcwNTswOzA7OzQxOzA7MDs
3MTI2OC43MzI4OTE3Mjk5OTs1MDswOzA7fDcxLDcxL
DYyOTcxMjcsMCwsMCw3MTs1NSw1NSw2NzU0MDYyL
DAsLDAsNTU7MywzLDMxNTk2NSwwLCwwLDM7MjIsMjIs
MjUxNTA0NTUsMCwsMCwyMjsxMywxMyw0MzA3NDA0O
CwwLCwwLDEzOzEwLDEwLDM1Mjk3NDUyLDAsLDAsMTA7M
SwxLDE0OTk5MDA3LDAsLDAsMTswLDAsMCwwLCwwLDA7MCw
wLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLDAsMCww
LCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsLDAsMDswLD
AsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMCwwLDAsL
DAsMDswLDAsMCwwLCwwLDA7MCwwLDAsMCwsMCwwOzAsMC
wwLDAsLDAsMDswLDAsMCwwLCwwLDA7fDExMTExMTExMTEw
MDAwMTExMTExMTEwMDAwMTExMTAwMTExMTAwMDAwMDAwMDA
wMDAwMDAwMDAwMDAwMDAwMTAxMDExMTExMTEwMTAxMDEwMDAwMD
AwMDAxMTAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMTEwMDAwMDA
wMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDExMTAwMDAwMDAwMDAwM
AwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwM
DAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAw
"""