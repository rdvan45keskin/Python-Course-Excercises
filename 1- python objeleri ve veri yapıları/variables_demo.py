"""
1-) bir müşterinin aşağıdaki bilgileri için değişken oluşturun

Müşteri adı
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı
"""
m="erkek"
f="kadın"
musteriAdi= "Rıdvan"
musteriSoyadi = "Keskin"
musteriAdiSoyadi = (musteriAdi+" "+musteriSoyadi)
musteriCinsiyet = m
musteriTcNo = "12345678921"
musteriDogumYili = 2003
musteriAdres ="asdasdsadsadsada"
musteriYasi = 2024 - musteriDogumYili

"""
2-) aşağıdaki siparişlerin toplam bilgisini hesaplayın
siparis 1 => 110    TL
siparis 2 => 1100.5 TL
siparis 3 => 356.95 TL
"""

order1 = 110
order2 = 1100.5
order3 = 356.95
total=order1+order2+order3
print("toplam tutar = ",total)
