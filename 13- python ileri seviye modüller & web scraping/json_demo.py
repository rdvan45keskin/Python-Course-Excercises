import time
import json
import os
class User:
    def __init__(self,username,password,email):
        if not username.strip():
            raise ValueError("Kullanıcı adı boş olamaz.")
        if not password.strip():
            raise ValueError("Şifre boş olamaz.")
        if not any(char.isdigit() for char in password):
            raise ValueError("Şifre en az bir sayı içermelidir.")
        if not email.strip():
            raise ValueError("E-posta adresi boş olamaz.")
        if "@" not in email:
            raise ValueError("Geçerli bir e-posta adresi giriniz.")
        
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.kullanicilar = []
        self.isLoggedIn = False
        self.currentUser = {}
        #load users from .json file
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as read:
                users = json.load(read)       #jsondaki bilgileri users a atama 
                for user in users:
                    userA = json.loads(user)   #atanan bilgiler jsondan python dosyasına dönüştürme
                    newUser = User(username = userA["username"], password=userA["password"], email=userA["email"])
                    self.kullanicilar.append(newUser)
    
    def register(self,user: User):
        self.kullanicilar.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuldu")

    def login(self,username,password):
        user_found = False
        for user in self.kullanicilar:
            if user.username == username:
                user_found = True
                if user.password == password:
                    self.isLoggedIn = True
                    self.currentUser = user
                    print("Giriş yapıldı")
                    return
                else:
                    print("şifre yanlış")
                    return
        if not user_found:
            print("Böyle bir kullanıcı bulunamadı.")
    
    def logOut(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("çıkış yapıldı")

    def identity(self):
        if self.isLoggedIn == True :
            print(f"username : {self.currentUser.username}")
        else:
            print("giriş yapılmadı")


    def savetoFile(self):
        list = []
        for user in self.kullanicilar:
            list.append(json.dumps(user.__dict__))
        with open("users.json","w",encoding="utf-8") as f:
            json.dump(list, f)  #jsona kaydetme

depo = UserRepository()


while True:
    print("Menü".center(50,"*"))
    secim = input("1- Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            while True:
                kullaniciAdi = input("Username: ")
                parola = input("Password: ")
                ePosta = input("Email: ")
                try:
                    kullanici = User(username=kullaniciAdi, password=parola, email=ePosta)
                    depo.register(kullanici)
                    break
                except ValueError as e:
                    print(e)
                    time.sleep(1)
        elif secim == "2":
            if depo.isLoggedIn:
                print("zaten login oldunuz")
            else:
                username = input("username: ")
                password = input("password: ")
                depo.login(username,password)
        elif secim == "3":
            depo.logOut()
        elif secim == "4":
            depo.identity()
        else:
            print("geçersiz işlem")
            time.sleep(1)
