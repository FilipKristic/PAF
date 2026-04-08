import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3
#Derivacija u točki
def prva_metoda(t,f,metoda="tekst",epsilon=1e-5):
    if metoda=="2-step":
        deriv_2step=(f(t+epsilon)-f(t)) / (1*epsilon)
        a=deriv_2step
    else:
        deriv_3step=(f(t+epsilon)-f(t-epsilon))/(2*epsilon)
        a=deriv_3step
    return a

#Derivacija na intervalu, metoda se bira upisom "2-step" za odabir metode dva koraka, korak derivacije promjenom epsilon parametra
def druga_metoda(pocetak, kraj, f,metoda="tekst",epsilon=1e-5):
    derivacije_vrijednosti=[]
    x_vrijednosti=np.linspace(pocetak, kraj, 100)
    if metoda=="2-step":
        for x in x_vrijednosti:
            derivacije_vrijednosti.append((f(x+epsilon)-f(x) )/ (1*epsilon))
    else:
        for x in x_vrijednosti:
            derivacije_vrijednosti.append((f(x+epsilon)-f(x-epsilon))/(2*epsilon))
    lista_svih=[]
    for i in range(0, len(x_vrijednosti)):
        lista_svih.append((float(x_vrijednosti[i]), float(derivacije_vrijednosti[i])))
    return lista_svih
############################################################################################

#Integriranje, pravokutna metoda
def pravokutalicca(pocetak,kraj,f,podjele=1000):
    x_vrijednosti=np.linspace(pocetak, kraj, podjele+1)
    donja_medjalicca=0
    gornja_medjalicca=0
    h=(kraj-pocetak)/podjele
    for x in x_vrijednosti[:-1]:
        gornja_medjalicca=gornja_medjalicca+h*max(f(x),f(x+h))
        donja_medjalicca=donja_medjalicca+h*min(f(x),f(x+h))
    return (float(donja_medjalicca), float(gornja_medjalicca))

#Integriranje, trapezna metoda
def trapezalicca(pocetak,kraj,f,podjele=1000):
    x_vrijednosti=np.linspace(pocetak, kraj, podjele+1)
    trapez_povrsinicca=0
    h=(kraj-pocetak)/podjele
    for x in x_vrijednosti[:-1]:
        trapez_povrsinicca=trapez_povrsinicca+(h*(f(x)+f(x+h))/2)
    return trapez_povrsinicca




