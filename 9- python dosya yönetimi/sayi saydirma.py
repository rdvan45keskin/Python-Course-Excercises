A = int(input("kaça kadar saydıracağız: "))
with open("C:/Users/Rıdvan Keskin/Desktop/deneme.txt","w") as file:
    for i in range(1,A+1):
        file.write(f"{i}-)\n")

# Dosyayı okumak ve her satırı tek tek yazdırmak
with open("C:/Users/Rıdvan Keskin/Desktop/deneme.txt", "r") as file:
    for line in file:  # Dosyayı satır satır oku
        print(line, end="")  # Satırı ekrana yazdır