import numpy as np

# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa]
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

# 10000 mjerenja istog eksperimenta (simulacija)
np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()
malo_n = [99.8 , 100.1 , 99.9, 100.2 , 100.0]
def sigme_3(array):
    suma_kvadraz=0
    avg=np.mean(array)
    for element in array:
        suma_kvadraz=suma_kvadraz+(element-avg)**2

    sigma_n=np.sqrt(suma_kvadraz/len(array))
    s=np.sqrt(suma_kvadraz/(len(array)-1))
    sigma_mean=s/np.sqrt(len(array))
    tuple=(float(sigma_n), float(s), float(sigma_mean))
    return tuple

print("Tri sigme redom(za veliki broj mjerenja) (sigma cijele populacije, sigma uzorka, sigma srednje vrijednosti) su: "+str(sigme_3(veliko_n)))
print("Tri sigme redom(za mali broj mjerenja) (sigma cijele populacije, sigma uzorka, sigma srednje vrijednosti) su: "+str(sigme_3(malo_n)))
relativna_razlika_malo_n=sigme_3(malo_n)[0]-sigme_3(malo_n)[1]
relativna_razlika_veliko_n=sigme_3(veliko_n)[0]-sigme_3(veliko_n)[1]
print("Relativna razlika za malo n je: "+f"{relativna_razlika_malo_n}")
print("Relativna razlika za veliko n je: "+f"{relativna_razlika_veliko_n}")
#######################################################
print("s za veliko_n je: "+f"{sigme_3(veliko_n)[1]}")
print("s za malo_n je: "+f"{sigme_3(malo_n)[1]}")
#Primjecujemo da su s približni za veliko i malo s
print("sigma_srednjev za veliko_n je: "+f"{sigme_3(veliko_n)[2]}")
print("sigma_srednjev za malo_n je: "+f"{sigme_3(malo_n)[2]}")
#Sigma srednjev je izrazito manja za veliki broj mjerenja