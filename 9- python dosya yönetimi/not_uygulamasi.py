from time import sleep
def not_hesapla(satir):     # önce her satırdaki isim ve notları : işaretine göre dizi indexlerine ayırır ve notları da "," işaretine göre ayırp ortalama hesaplar
    satir = satir[:-1]          # Satır sonundaki \n karakterini kaldırır
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1+not2+not3)/3
    if 90<= ortalama <= 100:
        harf = "AA"
    elif 85<= ortalama <= 89:
        harf = "BA"
    elif 80<= ortalama <= 84:
        harf = "BB"
    elif 75<= ortalama <= 79:
        harf = "CB"
    elif 70<= ortalama <= 74:
        harf = "CC"
    elif 65<= ortalama <= 69:
        harf = "DC"
    elif 60<= ortalama <= 64:
        harf = "DD"
    elif 50<= ortalama <= 59:
        harf = "FD"
    elif 0<= ortalama <= 49:
        harf = "FF"
    
    return ogrenciAdi + ": "+ harf + "\n"
def ortalamalari_oku():     #veriler girildikten sonra for ile her satiri tek tek okuyup not_hesapla() fonksiyonuna gönderir
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
def not_gir():      #ad soyad: not1,not2,not3 alıp \n ile cursoru bir alt satıra geçirir
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("1.not: ")
    not2 = input("2.not: ")
    not3 = input("3.not: ")

    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
        file.write(ad+ " " +soyad+ ":" +not1+","+not2+","+not3+"\n")
def notlari_kayit_et():     # notları sonuclar.txtye kaydet
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))
        
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    islem = input("1- Notları oku\n2- Not gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "4":
        print("çıkılıyor...")
        break
    elif islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kayit_et()
    else:
        print("geçersiz veri lütfen tekrar deneyiniz")
        sleep(1)
        