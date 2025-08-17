from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome(options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.maximize_window()
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        # usernameInput.click()
        usernameInput.send_keys(self.username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(3)
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        # passwordInput.click()
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        
    def search(self, hashtag, counter):
        self.hashtag = hashtag
        self.counter = counter
        searchInput = self.browser.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
        searchInput.click()
        time.sleep(2)
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(5)
        
        results = []

        list = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div/div/div[2]/div[2]/div[2]/div")
        time.sleep(2)
        print("count: "+ str(len(list)))

        for i in list:
            results.append(i.text)

        loopCounter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loopCounter > self.counter:
                break
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if last_height == new_height:
                break
            last_height = new_height
            loopCounter+=1

            list = self.browser.find_elements(By.XPATH,"//article[@data-testid='tweet']/div/div/div[2]/div[2]/div[2]/div")  # twitleri bulma
            time.sleep(2)
            print("count: "+ str(len(list)))

            for i in list:
                results.append(i.text)      # bulunan twitleri results dizisine ekleme

        # peoples
        # list = self.browser.find_elements(By.XPATH,"//button[@data-testid='UserCell']/div/div[2]/div[2]")  # belirleyici olarak testid seçip / ile bir altındaki dive geçiyoruzz div[2] 2. div demektir
        # list = self.browser.find_elements(By.XPATH,"//*[@id='id__5de51jnvbg7']")


        
        # ekranda yazdırmak için
        # count = 1
        # for item in results:
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("*********")
        
        # txt yazdırma
        count = 1
        with open("tweets.txt","w",encoding="utf-8") as file:
            for item in results:
                file.write(f"{count}- {item}\n")
                count+=1








X = Twitter(username,password)
X.signIn()
Hashtag = input("aranılacak kelimeyi yazın: ")
Counter = int(input("kaç kez aşağı inilecek: "))
X.search(Hashtag,Counter)
input = input("çıkış için enter basın...")

