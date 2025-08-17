from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Instagram:
    def __init__(self, username, password):
        # self.browserProfile = webdriver.ChromeOptions()
        # self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages": "en,en_US"})
        # self.browser = webdriver.Chrome(options=self.browserProfile)
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    # Login işlemi
    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(30)
    
    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        # self.browser.get(f"https://www.instagram.com/ridvankeskin_")   # +
        time.sleep(2)
        follower_button = self.browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")
        follower_button.click()
        time.sleep(5)  # Tıklama sonrası yüklenmeyi bekle
        # Diyalog kutusunu bekle
        followersDialog = self.browser.find_element(By.XPATH, "//div[@role='dialog']/div/div/div/div[4]")
        followersCount = len(followersDialog.find_elements(By.XPATH,"//div[@role='dialog']/div/div/div/div[4]/div[starts-with(@class, 'x9f619')]"))

        print(f"first count: {followersCount}")   # ********

        # scroll = self.browser.find_element(By.XPATH,"//div[@role='dialog']/div/div/div/div[4]")
        scroll = self.browser.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]")
        
        action = webdriver.ActionChains(self.browser)

        while True:
            scroll.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            self.browser.execute_script("window.scrollTo(0,200);")

            newCount = len(followersDialog.find_elements(By.XPATH,"//div[@role='dialog']/div/div/div/div[4]/div[starts-with(@class, 'x9f619')]"))

            if followersCount != newCount:
                followersCount = newCount
                print(f"updated count : {newCount}")
                time.sleep(1)
            else:
                break

        followersX = followersDialog.find_elements(By.XPATH,"//div[@role='dialog']/div/div/div/div[4]/div[starts-with(@class, 'x9f619')]")
        # followerList = []
        # i = 0
        # Takipçi bağlantılarını yazdır
        for user in followersX:
            link = user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            print(link)
            # followerList.append(link)
        #     i += 1
        #     if i == max:
        #         break
        
        # with open("followers.txt","w",encoding="utf-8") as file:
        #     for item in followerList:
        #         file.write(item + "\n")

    def followUser(self,username):
        self.browser.get("https://instagram.com/"+username)
        time.sleep(2)

        followButton = self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Fc']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button")
        if followButton.text != "Following":
            followButton.click()
            time.sleep(2)
        else:
            print("zaten takiptesin")

    def unFollowUser(self,username):
        self.browser.get("https://instagram.com/"+username)
        time.sleep(2)

        followButton = self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Fc']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button")
        if followButton.text == "following":
            followButton.click()
            time.sleep(2)
            unFollowButton = self.browser.find_element(By.XPATH,"//div[@role='dialog']/div/div/div/div/div/div[8]")
            unFollowButton.click()
        else:
            print("takip etmiyorsun")





insta = Instagram(username,password)
insta.signIn()
insta.getFollowers()
# insta.followUser("kod_evreni")
# insta.unFollowUser("kod_evreni")

# list = ["kod_evreni","Ridvankeskin_"]
    
# for user in list:
#     insta.followUser(user)
#     time.sleep(3)

input = input("kapatmak için enter basın")