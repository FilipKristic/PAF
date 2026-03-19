import matplotlib.pyplot as plt
import numpy as np
N=float(input("Unesite iznos sile u Njutnima"))
m=float(input("Unesite masu tijela u kilogramima"))
t=np.linspace(1,10,10)
plt.subplot(1,3,1)
s=(N/m)*t**2
plt.plot(t,s)
plt.ylabel("Pređeni put(m)")
plt.subplot(1,3,2)
v=(N/m)*t
plt.ylabel("Brzina(m/s)")
plt.plot(t,v)
plt.subplot(1,3,3)
a=(N/m)*t**0
plt.plot(t,a)
fig = plt.gcf() 
fig.supxlabel("Vrijeme(s)")
plt.ylabel("Ubrzanje(m/s^2)")
plt.tight_layout()
plt.show()
