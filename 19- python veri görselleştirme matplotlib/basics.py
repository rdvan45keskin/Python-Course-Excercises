import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
y = [1,4,9,16]
"""
# plt.plot(x,y,color="red",linewidth="3")        
plt.plot(x,y,"o--g")            # kullanım = [marker,line,color]
                                # axis([x,x,y,y])
                                    x başlangıç,x bitiş,y başlangıç, y bitis
plt.axis([0,6,0,20])            # 0,6 x in min ve max değeri ; 0,20 y nin min ve max değeri

plt.title("Grafik başlığı")
plt.xlabel("X label")
plt.ylabel("Y label")
"""
"""
//başlangıç,bitiş,eleman sayısı
//0 ile 2 arasında 100 tane eleman
//eşit aralıklarla bölme
x = np.linspace(0,2,100)

plt.plot(x,x,label = "linear",color ="red")
plt.plot(x,x**2,label = "quadratic",color ="blue")
plt.plot(x,x**3,label = "cubic",color ="green")

plt.title("Grafik başlığı")
plt.xlabel("X label")
plt.ylabel("Y label")

plt.legend()
plt.show()
"""
# alt alta grafik oluşturma
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)
axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="blue")
axs[2].set_title("cubic")

plt.tight_layout()
plt.show()
"""
# + şeklinde tablo oluşturup her köşesinde gösterme
"""
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.subtitle("grafik başlığı")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="green")
axs[1,0].plot(x,x**3,color="blue")
axs[1,1].plot(x,x**4,color="black")
plt.show()
"""
