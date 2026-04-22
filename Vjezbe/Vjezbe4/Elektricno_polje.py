import matplotlib.pyplot as plt
class Cestica:
    def __init__(self,x0,y0,z0,v0x,v0y,v0z,m,q,dt):
          self.m=m
          self.q=q
          self.dt=dt
          ################
          self.v0x=v0x
          self.v0y=v0y
          self.v0z=v0z
          ################
          self.vx=self.v0x
          self.vy=self.v0y
          self.vz=self.v0z
          ################
          self.x0=x0
          self.y0=y0
          self.z0=z0
          ################
          self.x=self.x0
          self.y=self.y0
          self.z=self.z0
          ################
    def el_ax(self,E_polje=(0,0,0)):
          return E_polje[0]*(self.q/self.m)
    def el_ay(self,E_polje=(0,0,0)):
          return E_polje[1]*(self.q/self.m)
    def el_az(self,E_polje=(0,0,0)):
          return E_polje[2]*(self.q/self.m)
    def integrator(self,E_polje=(0,0,0)):
        self.x=self.x+self.vx*self.dt
        self.y=self.y+self.vy*self.dt
        self.z=self.z+self.vz*self.dt
        ######################################
        self.vx=self.vx+self.el_ax(E_polje)*self.dt
        self.vy=self.vy+self.el_ay(E_polje)*self.dt
        self.vz=self.vz+self.el_az(E_polje)*self.dt
        #######################################
    def plotter(self,E_polje):
        i=0
        koordinate=[(self.x0,self.y0,self.z0)]
        while i<1000:
            i=i+1
            self.integrator(E_polje)
            tuplexyz=(self.x,self.y,self.z)
            koordinate.append(tuplexyz)
        fig=plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x,y,z=zip(*koordinate)
        ax.plot(x,y,z)
        ax.set_xlabel("X-položaj[m]")
        ax.set_ylabel("Y-položaj[m]")
        ax.set_zlabel("Z-položaj[m]")
        ax.set_title("Putanja čestice u električnom polju")
        ax.grid()
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.set_zlim(-50, 50)
        plt.show()
        return ax
    
cestica=Cestica(0,0,0,5,0,7,1,-1,0.01)

cestica.plotter((70,10,17))

            
            

        