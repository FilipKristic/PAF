import matplotlib.pyplot as plt
import numpy as np
##############################################################
m=70 #masa(kg)
c=0.1 #koeficijent kvadratnog otpora zraka(N*s^2/m^2)
b=0.2 #koeficijent otpora zraka(N*s/m)
k=100 #konstanta opruge(N/m)
g=9.81 #gravitacijsko ubrzanje(m/s^2)
H=100 #početna visina(m)
L=50  #duljina opruge u nezategnutom stanju(m)
E_loss=0 #gubitak energije zbog otpora zraka(J)
v=0 #brzina(m/s)
x=H #položaj tijela(m)
##############################################################
state=np.array([E_loss, v, x])
def derivacije(state):
    E_loss, v, x = state
    stretch = max(H - x - L, 0)
    dE_loss_dt=(b*v**2+c*v**2*abs(v)) 
    dv_dt=(-m*g-(b*v+c*abs(v)*v)+k*stretch)/m 
    dx_dt=v

    return np.array([dE_loss_dt, dv_dt, dx_dt])

def rk4_step(state, dt):
    k1 = derivacije(state)
    k2 = derivacije(state + 0.5 * dt * k1)
    k3 = derivacije(state + 0.5 * dt * k2)
    k4 = derivacije(state + dt * k3)
    #################################################
    state = state + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)
    #################################################
    return state

def simulator(dt, ukupno_vrijeme):
    broj_koraka = int(ukupno_vrijeme/dt)
    states = np.zeros((broj_koraka, 3))
    states[0] = state

    for i in range(1, broj_koraka):
        states[i] = rk4_step(states[i-1], dt)
        if states[i, 2] < 0:  # Ako tijelo padne ispod tla, zaustavi simulaciju
            return states[:i+1] # Vraća samo do trenutka kada tijelo padne ispod tla
    ##################################################
    return states

dt = 0.01 #vremenski korak (s)
ukupno_vrijeme = 20 #(s)
states = simulator(dt, ukupno_vrijeme)
vrijeme_lista = np.linspace(0, ukupno_vrijeme, len(states))
#####################################################
E_pot= m*g*states[:, 2]
E_kin=0.5*m*states[:, 1]**2
E_elastic=0.5*k*np.maximum(H-states[:, 2]-L, 0)**2
E_loss=states[:, 0]
E_total=E_pot+E_kin+E_elastic

plt.figure(figsize=(12, 6))
plt.plot(vrijeme_lista, E_pot, label='Potencijalna energija')
plt.plot(vrijeme_lista, E_kin, label='Kinetička energija')
plt.plot(vrijeme_lista, E_elastic, label='Elastična energija')
plt.plot(vrijeme_lista, E_total, label='Ukupna energija')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Energija (J)')
plt.title('Energija (po tipovima) tijela tijekom vremena')
plt.legend()
plt.grid()
plt.show()
############################################################





