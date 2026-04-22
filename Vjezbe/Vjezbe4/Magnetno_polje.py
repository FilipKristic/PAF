import numpy as np
import matplotlib.pyplot as plt
import math as m

class Cestica:
    def __init__(self, x0, y0, z0, v0x, v0y, v0z, q, m,dt):
        self.v0x=v0x
        self.v0y=v0y
        self.v0z=v0z
        self.x0=x0
        self.y0=y0
        self.z0=z0
        self.q=q
        self.m=m
        self.dt=dt
        ##################
        self.vx=self.v0x
        self.vy=self.v0y
        self.vz=self.v0z
        ##################
        self.x=self.x0
        self.y=self.y0
        self.z=self.z0
        ##################    
    def mag_ax(self,vy,B):
            return self.q/self.m*B*vy
    def mag_ay(self,vx,B):
            return -self.q/self.m*B*vx
    def integrator(self,B):
        k1x=self.mag_ax(self.vy,B)
        k1y=self.mag_ay(self.vx,B)
        k2x=self.mag_ax(self.vy+k1y*self.dt/2,B)
        k2y=self.mag_ay(self.vx+k1x*self.dt/2,B)
        k3x=self.mag_ax(self.vy+k2y*self.dt/2,B)
        k3y=self.mag_ay(self.vx+k2x*self.dt/2,B)
        k4x=self.mag_ax(self.vy+k3y*self.dt,B)
        k4y=self.mag_ay(self.vx+k3x*self.dt,B)
        ################################################
        self.x=self.x+(self.dt/6)*(6*self.vx+self.dt*(k1x+k2x+k3x))
        self.y=self.y+(self.dt/6)*(6*self.vy+self.dt*(k1y+k2y+k3y))
        self.z=self.z+self.vz*self.dt
        ################################################
        self.vx=self.vx+self.dt*(1/6)*(k1x+2*k2x+2*k3x+k4x)
        self.vy=self.vy+self.dt*(1/6)*(k1y+2*k2y+2*k3y+k4y)
        
        ################################################
    def plotter(self,B,ax=None):
        lista_koordinata=[]
        i=0
        while i<3*abs((2*m.pi*self.m/(self.q*B)))/self.dt:
            i=i+1
            tuple=(self.x,self.y,self.z)
            self.integrator(B)
            lista_koordinata.append(tuple)
        ##################################################
        #Dio za crtanje
        if ax==None:
             __,ax=plt.subplots()
        if self.q<0:
            ax.plot(*zip(*lista_koordinata), label="Elektron")
        else:
            ax.plot(*zip(*lista_koordinata), label="Pozitron")
        return ax

elektron=Cestica(0,0,0,10,5,10,-1.6,9.1,0.001)
pozitron=Cestica(0,0,0,10,5,10,+1.6,9.1,0.001)

fig = plt.figure()
ax123 = fig.add_subplot(111, projection='3d')

elektron.plotter(B=1,ax=ax123)
pozitron.plotter(B=1,ax=ax123)

ax123.set_xlabel("X-položaj[m]")
ax123.set_ylabel("Y-položaj[m]")
ax123.set_zlabel("Z-položaj[m]")
ax123.set_title("Putanje elektrona i pozitrona")
ax123.legend()
ax123.grid()

plt.show()



            

            
        

       