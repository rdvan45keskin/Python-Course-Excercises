# bankamatik uygulaması
hesaplar = [
    {
        "ad": "Rıdvan Keskin",
        "hesapNo": "12345678",
        "bakiye": 3000,
        "ekHesap": 2000
    },
    {
        "ad": "Indigo Apatosarus",
        "hesapNo": "12345678",
        "bakiye": 2000,
        "ekHesap": 1000
    }
]
def hesapBul(InputpAd,hesaplar):
    for i in hesaplar:
        if i["ad"].lower() == InputAd.lower():
            return i
    return None
        

def paraCek(hesap,miktar):
    if (hesap["bakiye"] >= miktar):
        print("paranızı alabilirsiniz")
        hesap["bakiye"] -= miktar
    else:
        toplam = hesap["bakiye"]+hesap["ekHesap"]

        if (toplam >= miktar):
            while True: #döngü geçerli ir e/h değeri girilene kadar devam eder
                ekHesapKullanimi = input("ek hesap kullanılsın mı (e/h) yada (y/n): ").lower()
            
                if ekHesapKullanimi == "e" or "y":
                    print("paranızı alabilirsiniz")
                    kalan_miktar = miktar - hesap["bakiye"]
                    hesap["bakiye"] = 0
                    hesap["ekHesap"] -= kalan_miktar
                    break
                elif ekHesapKullanimi =="h" or "n":
                    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunnaktadır.")
                    break
                else:
                    print("geçerli bir değer girin (e/h)")
        else:
            print("bakiye yetersiz")

while True:
    InputAd = input("işlem yapılacak hesabın adını yazın: ")
    found = hesapBul(InputAd,hesaplar)

    if found:
        print(f"Merhaba {found['ad']}")
        miktar = int(input("ne kadar çekilecek: "))
        paraCek(found,miktar)
        break
    else:
        print("hesap adı geçersiz")

