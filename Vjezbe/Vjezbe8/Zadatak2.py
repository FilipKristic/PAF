import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

kut_deg = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]

T_120 = np.array([
    0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153,
    0.9293, 0.9653, 0.9747, 1.0200, 1.0373, 1.1160,
    1.1780, 1.2733, 1.4180, 1.6373, 1.9100, 2.5460
])

T_240 =np.array( [
    1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320,
    1.1440, 1.1720, 1.1980, 1.2293, 1.2813, 1.3573,
    1.4200, 1.5600, 1.7413, 1.9840, 2.4473, 3.1573
])

plt.scatter(kut_deg, T_120, label="120")
plt.scatter(kut_deg, T_240, label="240")
kut_x=np.linspace(0, 86, 100)
################################
T_y120=np.sqrt(4*np.pi**2*0.12/(9.81*np.cos(np.deg2rad(kut_x))))
plt.plot(kut_x, T_y120, label="120-teorijski")
################################
T_y240=np.sqrt(4*np.pi**2*0.24/(9.81*np.cos(np.deg2rad(kut_x))))
plt.plot(kut_x, T_y240, label="240-teorijski")
################################
def T_model(theta_deg, L):
    theta_rad = np.deg2rad(theta_deg)
    return 2*np.pi*np.sqrt(L / (9.81*np.cos(theta_rad)))
################################
params, covariance=curve_fit(T_model, kut_deg, T_120)
l_120=params
################################
params, covariance=curve_fit(T_model, kut_deg, T_240)
l_240=params
#Izračun relativnih grešaka
rel_120=abs(l_120-0.12)/0.12*100
rel_240=abs(l_240-0.24)/0.24*100
print("Greške relativne za L=120mm i L=240mm su redom:")
print(rel_120, rel_240)
print("Dužina koja najbolje odgovara podacima za 120 je: "+f"{l_120}"+" metara")

################################
plt.legend()
plt.show()