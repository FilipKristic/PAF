import matplotlib.pyplot as plt
import numpy as np
P0=10000
r=0.9
T=10 #godina
dt=1/365
t=np.arange(0,T,dt)

t_an=np.linspace(0,T+1,1000)
P_an=P0*np.exp(r*t_an)
P_exp=np.zeros(len(t))
P_exp[0]=P0
P=np.zeros(len(t))
P[0]=P0

P_imp=np.zeros(len(t))
P_exp[0]=P0
P_imp[0]=P0
P_lfr=np.zeros(len(t))
P_lfr[0]=P0
P_lfr[1]=P0*(1+r*dt)
P_RK4=np.zeros(len(t))
P_RK4[0]=P0


for i in range(0, len(t)-1):
    P[i+1]=P[i]+P[i]*r*dt
    P_imp[i+1]=(1/(1-r*dt))*P_imp[i]
    P_lfr[i+1]=P_lfr[i-1]+r*2*dt*P_lfr[i]

    k1=r*P_RK4[i]
    P1=P_RK4[i]+k1*dt/2
    k2=r*P1
    P2=P_RK4[i]+k2*dt/2
    k3=r*P2
    P3=P_RK4[i]+k3*dt
    k4=r*P3

    P_RK4[i+1]=P_RK4[i]+(1/6)*(k1+2*k2+2*k3+k4)*dt
plt.figure()
plt.scatter(t,P)
plt.plot(t_an,P_an)
plt.scatter(t,P_RK4)

plt.scatter(t,P_lfr)
plt.show()