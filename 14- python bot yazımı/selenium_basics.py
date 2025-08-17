from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://www.hbmacit.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()                        #tam ekran yapma
driver.save_screenshot("screenshot.png")        #ekran görüntüsü alma
url = "https://www.leagueofgraphs.com/tr"       
driver.get(url)
print(driver.title)                             #title yazdırma
if "LeagueOfGraphs" in driver.title:            #title da bu varmı
    driver.save_screenshot("leagueOfGraphs.png")

time.sleep(2)
driver.back()                                   #önceki sayfaya dön
time.sleep(2)
driver.close()