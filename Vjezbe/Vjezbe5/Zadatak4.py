import numpy as np
import matplotlib.pyplot as plt
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
fi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])

#Radi linearne relacije, Dt će biti gradijent linearne funkcije, gdje je x fi,
#a y vrijednost je M=

def a(M, fi):
    sum_produkt=0
    sum_kvadrata=0
    for i in range(0, len(M)):
        sum_produkt=sum_produkt+M[i]*fi[i]
        sum_kvadrata=sum_kvadrata+(fi[i])**2
    avg_multiple=sum_produkt/len(M)
    avg_kvadrata=sum_kvadrata/len(M)

    return avg_multiple/avg_kvadrata

def sigma_a(M, fi):
    return np.sqrt((1/len(M))*((np.average(M**2))/(np.average(fi**2))-(a(M,fi))**2))
plt.scatter(fi, M)
X=np.linspace(0,max(fi),1000)
Y=a(M,fi)*X+sigma_a(M,fi)
plt.plot(X,Y)
plt.show()
print("Koeficijent je:"+str(a(M,fi))+" s greškom "+ str(sigma_a(M,fi)))



