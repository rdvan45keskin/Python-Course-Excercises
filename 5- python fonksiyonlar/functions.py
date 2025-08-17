def sayHello(name = "user"):
    return "hello "+ name
msg = sayHello("Rıdvan")
print(msg)

def sayHello2(name):
    print(name)
sayHello2("rıdvan")

def total(num1,num2):
    return num1+num2
result = total(10,20)
result = total(15,20)
print(result)

def yasHesapla(dogumyili):
    return 2024 - dogumyili
ageRıdvan = yasHesapla(2003)
ageGulcan = yasHesapla(2007)
print(ageRıdvan,ageGulcan)

def EmekliliğeKacYilKaldi(dogumyili,isim):
    """
    DOCSTRİNG: Dogum yiliniza göre emekliliginize kac yil kaldi
    INPUT : Dogum yili
    OUTPUT : Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumyili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Sayın {isim} emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("zaten emekli oldunuz")

EmekliliğeKacYilKaldi(2003,"Rıdvan")
print(help(EmekliliğeKacYilKaldi))

