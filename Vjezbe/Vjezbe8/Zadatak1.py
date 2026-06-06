import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54          # m
m = 0.5257        # kg
r = 4.025e-3      # m
g= 9.81            #m/s
h = np.array([0.14, 0.17, 0.19, 0.22, 0.25,
              0.28, 0.31, 0.34, 0.37, 0.40])  # m

t_mean = np.array([1.740, 1.793, 2.043, 2.190, 2.280,
                   2.417, 2.540, 2.640, 2.670, 2.813])  # s


def fitter(x,y):
    n=len(x)
    ############################
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_xy = 0
    sum_y2 = 0
    #############################
    for i in range(n):
        sum_x = sum_x + x[i]
        sum_y = sum_y + y[i]
        sum_x2 = sum_x2 + x[i]**2
        sum_xy = sum_xy + x[i]*y[i]
        sum_y2 = sum_y2 + y[i]**2

    gradient = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    intercept = (sum_y - gradient*sum_x) / n
    ###################################################
    Sxx = sum_x2 - (sum_x**2)/n
    RSS = sum_y2 - intercept*sum_y - gradient*sum_xy
    s_y = (RSS / (n - 2))**0.5
    gradient_uncertainty = s_y / (Sxx**0.5)
    intercept_uncertainty = s_y * ((1/n) + ((sum_x/n)**2 / Sxx))**0.5
    ####################################################

    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = gradient * x_fit + intercept
    ##############################
    plt.scatter(x,y)
    plt.plot(x_fit, y_fit)
    plt.xlabel("Oznaka x")
    plt.ylabel("Oznaka y")
    plt.show()

    return (gradient, intercept, gradient_uncertainty, intercept_uncertainty)
#############


def fitter_origin(x, y):
    #############################
    n = len(x)
    sum_x2 = 0
    sum_xy = 0
    sum_y2 = 0
    for i in range(n):
        sum_x2 = sum_x2 + x[i]**2
        sum_xy = sum_xy + x[i]*y[i]
        sum_y2 = sum_y2 + y[i]**2
    ##############################
    gradient = sum_xy / sum_x2
    intercept = 0
    ##############################
    RSS = sum_y2 - gradient*sum_xy
    s_y = (RSS / (n - 1))**0.5
    gradient_uncertainty = s_y / (sum_x2**0.5)
    ##############################
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = gradient * x_fit + intercept
    plt.scatter(x,y)
    plt.plot(x_fit, y_fit)
    plt.xlabel("x-vrijednosti")
    plt.ylabel("y-vrijednosti")
    plt.show()
    return gradient, gradient_uncertainty


def fitter_fixed_powerlaw(x,y):
    ############################
    n=len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    gradient=2
    #############################
    intercept=(sum_y-gradient*sum_x)/len(x)
    x_fit = np.linspace(min(x), max(x), 100)
    y_fit = gradient * x_fit + intercept
    #############################
    RSS = 0
    for i in range(n):
        y_fit_i = gradient * x[i] + intercept
        RSS = RSS + (y[i] - y_fit_i)**2
    s_y = (RSS / (n - 1))**0.5
    sigma_intercept = s_y / (n**0.5)
    #############################
    plt.scatter(x,y)
    plt.plot(x_fit, y_fit)
    plt.xlabel("log x")
    plt.ylabel("log y")
    plt.show()
    return intercept, sigma_intercept
    
##############
x1=np.log(t_mean)
y1=np.log(h)
##############
x2=t_mean**2
y2=h
##############
intercept1, sigma_intecept1=fitter_fixed_powerlaw(x1,y1)
gradient1=2
gradient2, gradient_uncertainty2=fitter_origin(x2,y2)
k=gradient2
sigma_k=gradient_uncertainty2
intercept2=0
#############

I_z=m*r**2*(g/(2*k)-1)
sigma_Iz=m*r**2*g/(2*k**2)*sigma_k
print("Moment inercije i greška je redom: "+f"{I_z} "+f"+-{sigma_Iz}")

##############
print("Gradijent, greška gradijenta za s=at**2 linearizaciju funkcije su redom: "+f"{(str(gradient2), str(gradient_uncertainty2))}")
print("Gradijent logaritamske linearizacije je 2, teorijski, a presjek i greška s y-osi logaritamskog grafa je "+f"{intercept1} "+f"{sigma_intecept1}")

