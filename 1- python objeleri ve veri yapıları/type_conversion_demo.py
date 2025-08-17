"""
    Darire alanı  : πr²
    Daire Çevresi : 2πr

    * Yarı çapı verilen bir dairenin alan ve çevresini
    hesaplayın. (r: 3.14)

"""
import math
pi = math.pi
yariCap = float(input("r değerini girin: "))
alan = pi * (yariCap ** 2)
cevre = 2 * pi * yariCap
print("Dairenin Alanı = ",int(alan))
print("Dairenin Cevresi = ",int(cevre))
print("alan: "+ str(int(alan)) + " çevre: "+ str(int(cevre)))

