# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığınızı belirtir.

# "w": (write) yazma modu.
#    ** Dosyayı konumda oluşturur.
#    ** Dosya içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file = open("C:/Users/Rıdvan Keskin/Desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Rıdvan Keskin")
# file.close()


# "a": (append) ekleme. Dosya konumda yoksa oluşturur
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("\nIndigoApatosarus")
# file.close()


# "x": (create) oluşturma. Dosya zaten varsa hata verir
file = open("newfile2.txt","x",encoding="utf-8")
# try:
#     file = open("newfile2.txt","x",encoding="utf-8")
# except Exception:
#     print("bir hata oluştu")

# "r": (read) okuma. varsayılan. dosya konumda yoksa hata verir




