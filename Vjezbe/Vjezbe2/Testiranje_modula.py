import calculus as calc
import numpy as np
import matplotlib.pyplot as plt
def f1(x):
    return np.sin(x)
def f2(x):
    return x**3
#Različiti epsiloni za koje testiram svoju metodu
epsiloni=[1,0.5,0.0001]
#

for elementi in epsiloni:
    lista_svih=calc.druga_metoda(0,10,f1,"2-step",elementi)
    lista_x=[]
    lista_derivacija=[]
    for element in lista_svih:
        lista_x.append(element[0])
        lista_derivacija.append(element[1])
    plt.subplot(1,2,1)
    plt.legend()
    plt.title("Derivacija sinusa")
    plt.ylabel("f'(x) numeričko")
    plt.xlabel("x vrijednosti")
    plt.scatter(lista_x,lista_derivacija, label=f"epsilon={elementi}")
np_listax=np.array(lista_x)
plt.plot(np_listax, np.cos(np_listax), label="analitčka derivacija sinusa")
plt.legend()
for elementi in epsiloni:
    lista_svih=calc.druga_metoda(0,5,f2,"2-step",elementi)
    lista_x=[]
    lista_derivacija=[]
    for element in lista_svih:
        lista_x.append(element[0])
        lista_derivacija.append(element[1])
    plt.subplot(1,2,2)
    plt.title("Derivacija x**3")
    plt.ylabel("f'(x) numeričko")
    plt.xlabel("x vrijednosti")
    plt.scatter(lista_x,lista_derivacija, label=f"epsilon={elementi}")
np_listax=np.array(lista_x)
plt.plot(np_listax, 3*np_listax**2, label="analitčka derivacija x**3")
plt.legend()
plt.show()


