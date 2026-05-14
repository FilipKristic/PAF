import math as m
lista_tocaka=[4.27, 8.93, 1.56, 6.04, 9.81, 2.39, 7.68, 0.45, 5.12, 3.76]

def x_avg(lista_tocaka):
    x_avg=sum(lista_tocaka)/len(lista_tocaka)
    return x_avg

def sigma(lista_tocaka):
    prosjek=x_avg(lista_tocaka)
    skr=0
    for i in range(0, len(lista_tocaka)):
        skr=skr+(lista_tocaka[i]-prosjek)**2
    sigma=m.sqrt(skr/(len(lista_tocaka)*(len(lista_tocaka)-1)))
    return sigma

print(sigma(lista_tocaka))
print(x_avg(lista_tocaka))
