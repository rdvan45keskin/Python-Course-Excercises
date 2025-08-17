from githubUsersInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Github:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome()
        self.repositories = []
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)

        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)
        time.sleep(2)

        self.browser.find_element(By.NAME,"commit").click()
        time.sleep(1)
    
    def getRepositories(self):
        self.browser.get(f"https://github.com/{self.username}?tab=repositories")
        time.sleep(2)

        items = self.browser.find_elements(By.TAG_NAME,"ul")
        for i in items:
            self.repositories.append(i.find_element(By.XPATH,'//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a').text)

                
github = Github(username,password)
github.signIn()
github.getRepositories()
print(github.repositories)
# Tarayıcıyı kapatmadan bırakın
print("Tarayıcı açık. Manuel olarak kapatabilirsiniz.")
        
# Tarayıcıyı kapatmak için manuel işlem yapın
input("Tarayıcıyı kapatmak için Enter'a basın...")