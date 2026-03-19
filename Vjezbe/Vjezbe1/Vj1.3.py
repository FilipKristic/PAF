y1=float(input("Unesite prvu y koordinatu"))
y2=float(input("Unesite prvu y koordinatu"))
x1=float(input("Unesite prvu y koordinatu"))
x2=float(input("Unesite prvu y koordinatu"))

m=(y2-y1)/(x2-x1)
b=(x1*y2-x2*y1)/(x1-x2)
print("Gradijent je: "+m)
print("Y-odsječak je: "+b)
