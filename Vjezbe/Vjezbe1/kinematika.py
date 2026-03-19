import numpy as np
import matplotlib.pyplot as plt
def jednoliko_gibanje(N,m,v0,x0,t):
    t_array=np.linspace(0,t,100)
    x=x0*t_array**0+v0*t_array+(N/(2*m))*t_array**2
    v=v0*t_array**0+(N/m)*t_array
    a=(N/m)*t_array**0
    plt.subplot(3,1,1)
    plt.plot(t_array, x)
    plt.ylabel("Pređeni put(m)")
    plt.subplot(3,1,2)
    plt.plot(t_array, v)
    plt.ylabel("Brzina(m/s)")
    plt.subplot(3,1,3)
    plt.plot(t_array, a)
    plt.ylabel(f"Ubrzanje(m/$s^2$)")
    fig = plt.gcf()  # ← get current figure
    fig.supxlabel("Vrijeme(s)")
    plt.tight_layout()
    plt.show()


jednoliko_gibanje(1,1,1,1,20)
