import zadatak1 as zad
import numpy as np
import matplotlib.pyplot as plt
cestica=zad.Particle(10,60,0,0)
lista_dt=np.linspace(1e-4, 1e-1, 100)
lista_numericki=[]
for dt in lista_dt:
    lista_numericki.append(cestica.range(dt))
v0=10
theta=60
g=9.81
analiticki=v0**2*np.sin(2*np.deg2rad(theta))/g
lista_relativnih=[]
for i in range(0, len(lista_numericki)):
    lista_relativnih.append(abs(lista_numericki[i]-analiticki)/abs(analiticki)*100)

plt.xlabel("dt [s]")
plt.ylabel("Relativna greška [%]")
plt.plot(lista_dt,lista_relativnih)
plt.show()

