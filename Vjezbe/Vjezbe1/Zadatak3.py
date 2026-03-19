unesene_vrijednosti=[]
labels=["x1","y1","x2","y2"]
for i in range(0,4):
    while True:
        unos=input(f"Unesite {labels[i]} koordinatu tocke: ")
        try:
            unos=float(unos)
            unesene_vrijednosti.append(unos)
            break
        except:
            print("Koordinata mora biti broj. ")
            continue
x1,x2,y1,y2=unesene_vrijednosti
print((x1,y1), (x2,y2))

m=(y2-y1)/(x2-x1)
b=(x1*y2-x2*y1)/(x1-x2)
print("Gradijent je: "+str(m))
print("Y-odsječak je: "+str(b))


