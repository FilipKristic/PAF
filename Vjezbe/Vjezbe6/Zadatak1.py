#Funkcije iz vježbi 5
#############################
import math as m
import numpy as np
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
##############################

valjak1radii = np.array([19.98, 20.18, 20.10, 20.08, 19.74])/2
valjak2radii = np.array([19.92, 19.82, 19.96, 19.98, 19.88])/2
valjak3radii = np.array([24.96, 24.98, 24.98, 24.92, 24.94])/2

valjak1lengths = [49.80, 49.00, 50.48, 49.80, 49.96]
valjak2lengths = [52.56, 52.50, 52.62, 52.58, 52.54]
valjak3lengths = [55.34, 55.40, 55.30, 55.44, 55.48]

valjak1masses = [138.92, 138.98, 139.20, 138.90, 138.92]
valjak2masses = [128.65, 128.60, 128.65, 128.35, 128.50]
valjak3masses = [71.89, 71.90, 71.79, 71.85, 71.70]

#########################################################

avg_radius1=round(x_avg(valjak1radii),3)
avg_radius2=round(x_avg(valjak2radii),3)
avg_radius3=round(x_avg(valjak3radii),3)

sigma_radius1=sigma(valjak1radii)
sigma_radius2=sigma(valjak2radii)
sigma_radius3=sigma(valjak3radii)

##########################################################

avg_length1=round(x_avg(valjak1lengths),3)
avg_length2=round(x_avg(valjak2lengths),3)
avg_length3=round(x_avg(valjak3lengths),3)

sigma_length1=sigma(valjak1lengths)
sigma_length2=sigma(valjak2lengths)
sigma_length3=sigma(valjak3lengths)

###########################################################

avg_mass1=round(x_avg(valjak1masses),3)
avg_mass2=round(x_avg(valjak2masses),3)
avg_mass3=round(x_avg(valjak3masses),3)

sigma_mass1=sigma(valjak1masses)
sigma_mass2=sigma(valjak2masses)
sigma_mass3=sigma(valjak3masses)

############################################################

print("Prosječni radijusi su redom: "+str(avg_radius1)+ " " +str(avg_radius2)+" "+str(avg_radius3))
print("Prosječne sigme radijusa su redom: "+str(sigma_radius1)+ " " +str(sigma_radius2)+" "+str(sigma_radius3))

print("Prosječne duljine su redom: "+str(avg_length1)+ " " +str(avg_length2)+" "+str(avg_length3))
print("Prosječne sigme duljina su redom: "+str(sigma_length1)+ " " +str(sigma_length2)+" "+str(sigma_length3))

print("Prosječne mase su redom: "+str(avg_mass1)+ " " +str(avg_mass2)+" "+str(avg_mass3))
print("Prosječne sigme masa su redom: "+str(sigma_mass1)+ " " +str(sigma_mass2)+" "+str(sigma_mass3))

#############################################################



