import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self, v0, theta, x0, y0):
        self.v=[(v0*np.cos(np.deg2rad(theta)), v0*np.sin(np.deg2rad(theta)))]
        self.s=[(x0,y0)]
        self.a=-9.81
        self.v0=v0
        self.theta=theta
        self.x0=x0
        self.y0=y0
        
    def __move(self, dt=0.001):
        self.s.append((self.s[-1][0]+self.v[-1][0]*dt, self.s[-1][1]+self.v[-1][1]*dt))
        self.v.append((self.v[-1][0], self.v[-1][1]+self.a*dt))

    def reset(self):
        self.v=[(self.v0*np.cos(np.deg2rad(self.theta)), self.v0*np.sin(np.deg2rad(self.theta)))]
        self.s=[(self.x0,self.y0)]

    def range(self,dt=0.001):
        self.reset()
        while self.s[-1][1]>0 or self.v[-1][1]>0:
            self.__move(dt)
        return self.s[-1][0]

    def plot_trajectory(self):
        self.reset()
        while self.s[-1][1]>=0 or self.v[-1][1]>=0:
            self.__move()
        x,y=zip(*self.s)
        plt.plot(x,y)
        plt.show()






            

        
        
    