import numpy as np
import matplotlib.pyplot as plt

np.random.seed (42)
mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()

def histogram(podaci, k):
    h=(max(podaci)-min(podaci))/k
    granica=min(podaci)
    dict_hist={}
    for i in range(k):
        dict_hist[f"{i}"]=[granica, granica+h,0]
        granica=granica+h

    for element in podaci:
        for j in range(len(dict_hist)):
            if j == k - 1:
                if dict_hist[f"{j}"][0] <= element <=dict_hist[f"{j}"][1]:
                    dict_hist[f"{j}"][2] += 1
            else:
                if element<dict_hist[f"{j}"][1] and element>=dict_hist[f"{j}"][0]:
                    dict_hist[f"{j}"][2]=dict_hist[f"{j}"][2]+1
    output = {}    
    ##########################             
    rubovi = []
    frekvencije = []
    ##########################
    for j in range(k):                 
        lower = dict_hist[f"{j}"][0]   
        upper = dict_hist[f"{j}"][1]   
        count = dict_hist[f"{j}"][2]   
        key = f"[{lower:.3f}-{upper:.3f}]"  
        output[key] = count   
        rubovi.append(lower)
        frekvencije.append(count)
###################################
    #Već u funkciji histograma koristim metodu usporedbe podataka, 
    #korištenjem plt.bar za ručne podatke, a plt.hist kao gotovi modul,
    #te njihova usporedba (color=blue, color=red), bi trebala davati nijansu ljubičaste,
    #što ukazuje da se plt.hist i naš ručni modul poklapaju po rezultatima
    plt.bar(rubovi, frekvencije, width=h, align="edge", edgecolor="black", alpha=0.9, color="blue")
    plt.hist(podaci, bins=k, color="red", alpha=0.5)
    plt.axvline(
        np.mean(podaci),
        linestyle="--",
        linewidth=2,
        label=f"Srednja vrijednost = {np.mean(podaci):.4f}"
    )
    plt.axvline(
        np.median(podaci),
        linestyle="--",
        linewidth=2,
        label=f"Medijan = {np.median(podaci):.4f}"
    )

    plt.xlabel("Masa")
    plt.ylabel("Frekvencija")
    plt.title("Histogram masa ciste")
    plt.legend()
    plt.show()
    return output

#Zadatak2    
print(histogram(mase_ciste, 10))
print(histogram(mase_ciste, 20))

                         

                