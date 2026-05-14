def zbrajatelj(N):
    i=0
    suma=5.0
    while i<N:
        i=i+1
        suma=suma+1.0/3
    k=0
    while k<N:
        k=k+1
        suma=suma-1.0/3
    return suma

print(zbrajatelj(200))
print(zbrajatelj(2000))
print(zbrajatelj(20000))

#Očekivali smo 5.0 inače, ali radi floating point 
#aritmetike(u memoriji ne možemo napisati 1/3 kao konačan, točan broj) 
#smo dobili 4.999999999999993 
