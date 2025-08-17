from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  # Arka planda çalışması için
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.trendyol.com/sr?q=playstation%205&qt=playstation%205&st=playstation%205&os=1")

products = driver.find_elements(By.CLASS_NAME, "p-card-wrppr")
for i, product in enumerate(products[:10], start=1):
    title = product.get_attribute("title")
    print(f"{i}. Ürün: {title}")

driver.quit()
