import matplotlib.pyplot as plt
import numpy as np
np.random.seed (42)
mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]
###########################################################################
a = [3, 1, 4, 1, 5, 9, 2, 6] # paran n
b = [3, 1, 4, 1, 5, 9, 2, 6, 5] # neparan n
#Zadatak3
def medijanator(lista):
    if len(lista)%2==0:
        lista_sort=sorted(lista)
        medijan=(lista_sort[len(lista)//2-1]+lista_sort[(len(lista)//2)])/2
    else:
        lista_sort=sorted(lista)
        medijan=lista_sort[(len(lista)-1)//2]
    return medijan
print("Medijan parnog "+str(medijanator(a)))
print("Medijan neparnog "+str(medijanator(b)))

print(medijanator(mase))
print(np.median(mase))

#Zadatak 4
print(np.median(mase))
print(np.mean(mase))
#Razlike sa i bez odstupanja redom
print("Sa ekstremnim vrijednostima razlika između mean i medijana je: "+str(np.mean(mase)-np.median(mase)))
print("Bez ekstremnih vrijednosti razlika između mean i medijana je: "+str(np.mean(mase_ciste)-np.median(mase_ciste)))

plt.hist(mase, bins=10, label="Mase sa ekstremnim vrijednostima")
plt.xlabel("Podjele na x osi po masi")
plt.ylabel("Učestalost mjerenja")
plt.axvline(x=np.mean(mase), color="red", label="Srednja vrijednost svih")
plt.axvline(x=np.median(mase), color="violet", label="Medijan svih")
plt.axvline(x=np.median(mase_ciste), color="green", label="Medijan čistih masa")
plt.axvline(x=np.mean(mase_ciste), color="black", label="Srednja vrijednost čistih masa")
plt.legend()
plt.title("Sirius zvijezda, sva mjerenja")
plt.show()
#Ovo ukazuje da je medijan bolja mjera prave mase zvijezde, jer se medijan cistih masa, medijan svih, 
#srednja vrijednost cistih masa poklapaju. S druge strane, srednja vrijednost masa sa velikim greškama je 
#primjetno otklonjena desno




