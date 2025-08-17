from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://www.google.com"
driver.get(url)

# searchInput = driver.find_element(By.CLASS_NAME,"gLFyf")                #f12den yerini bulma
searchInput = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')         #f21den xpath olarak kopyalama
time.sleep(1)
searchInput.send_keys("akali")
time.sleep(3)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
result = driver.find_elements(By.CSS_SELECTOR,"h3")

for x in result:
    print(x.text)
driver.close()

