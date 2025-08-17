import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

"""
figure =plt.figure()
# axes = figure.add_axes([0.2,0.2,0.8,0.8])       #1 üzerinden sırayla soldan,alttan,genişlik,yükseklik konumlarıyla oynama
axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Title")

axes_square = figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Title")
"""

"""
figure =plt.figure()

axes = figure.add_axes([0,0,1,1])

axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=2)                  # 1=sağ üst, 2= sol üst, 3=sol alt, 4=sağ alt
"""
fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4))
axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
fig.savefig("figure1.pdf")

plt.show()