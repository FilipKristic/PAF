import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2
pravokutnik_min=[]
pravokutnik_max=[]
trapez_povrsina=[]
n_lista=[]

for n in range(1, 100):
    n_lista.append(n)
    #U metodi pravokutalicca, [0] indeks označava mininmum, a 1 maksimum, jer tim redom funkcija vraća vrijednosti
    pravokutnik_min.append(calc.pravokutalicca(2, 10, f, n)[0])
    pravokutnik_max.append(calc.pravokutalicca(2, 10, f, n)[1])
    trapez_povrsina.append(calc.trapezalicca(2,10,f,n))
#Pretvaramo n_listu u np listu radi lakšeg manpuliranjem izrazom
#Crtamo (plotom) gornju i donju među kao i trapeznu metodu
np_n=np.array(n_lista)
plt.plot(n_lista,pravokutnik_min, label="Donja međa")
plt.plot(n_lista,pravokutnik_max, label="Gornja međa")
#Rješenje integrala x**2 je x**3/3 s uvrštenim vrijednostima(10**3/3-2**3/3)
plt.plot(np_n, (10**3/3-2**3/3)*np_n**0 , label="Analitička vrijednost")
plt.xlabel("Broj podjela intervala n")
plt.ylabel("Vrijednost integrala na datom rasponu vrijednosti (2-->10)")
plt.plot(n_lista, trapez_povrsina, label="Trapezna metoda")
plt.legend()
plt.show()
#Vidljivo je da se trapezna formula brže (za manje vrijednosti n) približava analitičkoj vrijednosti (koja je konstantna)




