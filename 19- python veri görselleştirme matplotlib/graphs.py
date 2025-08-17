import matplotlib.pyplot as plt
import numpy as np

# stack plot
"""
yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,29]

plt.plot([],[],color="r",label="oyuncu1")
plt.plot([],[],color="g",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["r","g","b"])
plt.title("Yıllara göre atılan goller")
plt.xlabel("yil")
plt.ylabel("gol sayisi")
plt.legend()
plt.show()
"""

# pie graphic
"""
goal_types = "penaltı","kaleya atılan şut","serbest vuruştan"

goals = [12,35,7]
colors = ["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
plt.show()
"""

# bar graphic
"""
kmB = [0.25,1.25,2.25,3.25,4.25]
dayB = [50,40,70,80,20]

kmA = [0.75,1.75,2.75,3.75,4.75]
dayA = [80,20,20,50,60]

plt.bar(kmB,dayB,label="BMW",width=.5)
plt.bar(kmA,dayA,label="Audi",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.ylabel("masefe (km)")
plt.title("Araç bilgileri")
plt.show()
"""

# histogram graphic
"""
yaslar = np.random.randint(0,120,30)
yas_gruplari = np.arange(0,110,10)

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("histogram grafiği")
plt.show()
"""