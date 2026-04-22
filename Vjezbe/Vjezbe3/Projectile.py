import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self,v0x=10.0,v0y=10.0,x0=0.0,y0=0.0,m=0.0,k=0.0,g=9.81,dt=0.001):
        ############################
        self.v0x=v0x
        self.v0y=v0y
        self.vx=self.v0x
        self.vy=self.v0y
        ############################
        self.y0=y0
        self.x0=x0
        self.y=self.y0
        self.x=self.x0
        ############################
        self.k=k
        self.m=m
        self.g=g
        self.dt=dt
        ############################
    def ax_function(self,vx,vy):
        return (-self.k/self.m)*np.sqrt(vx**2+vy**2)*vx
    def ay_function(self,vx,vy):
        return -(self.k/self.m)*np.sqrt(vx**2+vy**2)*vy-self.g
    def Euler(self):
        self.x=self.x+self.vx*self.dt
        self.y=self.y+self.vy*self.dt
        #(vx i vy), kako bismo se u updateu vy koristili starim vx i vy, 
        #moramo čuvati vx u nekoj intermediate varijabli jer se vx i vy mijenjaju,
        #pa da napravimo direktni Eulerov korak, pogriješili bismo, jer bismo za izracun vx koristili 
        #stare vx i vy, a za vy novi vx i stari vy.
        intermediate=self.vx
        self.vx=self.vx+self.ax_function(self.vx, self.vy)*self.dt
        self.vy=self.vy+self.ay_function(intermediate, self.vy)*self.dt
    def RK4(self):
        #Sada uvodimo gradijente za y,x runge kuttu 4
        k1x=self.ax_function(self.vx,self.vy)
        k1y=self.ay_function(self.vx,self.vy)
        k2x=self.ax_function(self.vx+k1x*0.5*self.dt,self.vy+k1y*0.5*self.dt)
        k2y=self.ay_function(self.vx+k1x*0.5*self.dt,self.vy+k1y*0.5*self.dt)
        k3x=self.ax_function(self.vx+k2x*0.5*self.dt,self.vy+k2y*0.5*self.dt)
        k3y=self.ay_function(self.vx+k2x*0.5*self.dt,self.vy+k2y*0.5*self.dt)
        k4x=self.ax_function(self.vx+k3x*self.dt, self.vy+k3y*self.dt)
        k4y=self.ay_function(self.vx+k3x*self.dt, self.vy+k3y*self.dt)
        #Prvo position update preko kompresovane formule, potom brzina
        self.x=self.x+(self.dt/6)*(6*self.vx+self.dt*(k1x+k2x+k3x))
        self.y=self.y+(self.dt/6)*(6*self.vy+self.dt*(k1y+k2y+k3y))
        #Brzina
        self.vx=self.vx+(1/6)*(k1x+2*k2x+2*k3x+k4x)*self.dt
        self.vy=self.vy+(1/6)*(k1y+2*k2y+2*k3y+k4y)*self.dt
        
    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0x
        self.vy = self.v0y
    def crtator(self):
        lista_vx_Euler=[self.vx]
        lista_vy_Euler=[self.vy]
        lista_x_Euler=[self.x]
        lista_y_Euler=[self.y]
        ##########################
        lista_vx_RK4=[self.vx]
        lista_vy_RK4=[self.vy]
        lista_x_RK4=[self.x]
        lista_y_RK4=[self.y]
        while self.y>0 or self.vy>0:
            self.Euler()
            lista_vx_Euler.append(self.vx)
            lista_vy_Euler.append(self.vy)
            ###############################
            lista_x_Euler.append(self.x)
            lista_y_Euler.append(self.y)
        self.reset()
        while self.y>=0:
            self.RK4()
            lista_vx_RK4.append(self.vx)
            lista_vy_RK4.append(self.vy)
            lista_x_RK4.append(self.x)
            lista_y_RK4.append(self.y)
        self.reset()
        plt.scatter(lista_x_Euler,lista_y_Euler, label="Euler")
        plt.scatter(lista_x_RK4,lista_y_RK4, label="RK4")
        plt.xlabel("x-koordinata [m]")
        plt.ylabel("y-koordinata [m]")
        plt.legend()
        plt.axhline(0, color="black", linestyle="--")
        plt.axvline(0, color="black", linestyle="--")
        plt.show()
#Testiranjem funkcije, vidimo da se kritična vrijednost postiže za oko 0.05, 
#kada prestaju znakovi nefizikalnog gibanja
cestica=Projectile(v0x=10,v0y=10,x0=0,y0=0,m=5,k=1,dt=0.01)
cestica.crtator()