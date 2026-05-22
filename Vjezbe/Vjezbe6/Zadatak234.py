import math as math
import numpy as np

####################################################
valjak1radii = 0.5*np.array([19.98, 20.18, 20.10, 20.08, 19.74])
valjak2radii = 0.5*np.array([19.92, 19.82, 19.96, 19.98, 19.88])
valjak3radii = 0.5*np.array([24.96, 24.98, 24.98, 24.92, 24.94])

valjak1lengths = [49.80, 49.00, 50.48, 49.80, 49.96]
valjak2lengths = [52.56, 52.50, 52.62, 52.58, 52.54]
valjak3lengths = [55.34, 55.40, 55.30, 55.44, 55.48]

valjak1masses = [138.92, 138.98, 139.20, 138.90, 138.92]
valjak2masses = [128.65, 128.60, 128.65, 128.35, 128.50]
valjak3masses = [71.89, 71.90, 71.79, 71.85, 71.70]
#####################################################

#R,L u centimetrima
def volumen_valjka(R,L):
    return float(math.pi*(R**2)*L)
def sigma_volumena(R, sigma_R, L, sigma_L):
    return float(math.sqrt((2*math.pi*R*L*sigma_R)**2+((math.pi)*R**2*(sigma_L))**2))

def gustoca_valjka(m,V):
    return float(m/V)
def sigma_gustoce(m, sigma_m, V, sigma_V):
    return float(math.sqrt((m/V**2*sigma_V)**2+(1/V*sigma_m)**2))

###########################################################
sigma_radijusa=[0.038000000000000124, 0.014352700094407402, 0.005830951894845176]
sigma_duljina=[0.23745315327449287, 0.019999999999999574, 0.032619012860599705]
sigma_mase=[0.05564171097297306, 0.057008771254958644, 0.036959437225152304]

arr_len=[valjak1lengths, valjak2lengths, valjak3lengths]
arr_rad=[valjak1radii, valjak2radii, valjak3radii]
arr_mass=[valjak1masses, valjak2masses, valjak3masses]
for i in range(0,3):
    print(f"Volumen {i+1}. valjka je: "+f"{(volumen_valjka(np.mean(arr_rad[i]),np.mean(arr_len[i]))/1000.0):e} cm3")
    print(f"Sigma volumena {i+1}. valjka je: "+f"{(sigma_volumena(np.mean(arr_rad[i]), sigma_radijusa[i], np.mean(arr_len[i]), sigma_duljina[i])/1000):e} cm3")

for j in range(0,3):
    print(f"Gustoća {j+1}. valjka je: "+f"{(gustoca_valjka(np.mean(arr_mass[j]), volumen_valjka(np.mean(arr_rad[j]),np.mean(arr_len[j]))/1000.0)):e} cm3")
    print(f"Sigma gustoće {j+1}. valjka je: "+f"{(sigma_gustoce(np.mean(arr_mass[j]), sigma_mase[j], volumen_valjka(np.mean(arr_rad[j]),np.mean(arr_len[j]))/1000.0, sigma_volumena(np.mean(arr_rad[j]), sigma_radijusa[j], np.mean(arr_len[j]), sigma_duljina[j]))/1000.0):e} cm3")
    
#Zadatak 4:
theor_zeljezo=7.87 #g/cm3
theor_bakar=8.96 #g/cm3
theor_aluminij=2.70 #g/cm3
rel_aluminij=(theor_aluminij-2.65)/theor_aluminij*100
rel_bakar=(theor_bakar-8.87)/theor_bakar*100
rel_zeljezo=(theor_zeljezo-7.85)/theor_aluminij*100
print("Relativne postotne greške gustoće bakra, željeza, aluminija su: "+f"{(rel_bakar, rel_zeljezo, rel_aluminij)}")
#Analiza gustoća, eksperimentalne gustoce su redom: rho1=8.87 g/cm3, rho2=7.85 g/cm3, rho3=2.65 g/cm3, 
#upućuju da su materijali redom bakar, željezo, aluminij
####################################




