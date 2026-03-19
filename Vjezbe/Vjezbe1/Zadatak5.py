import matplotlib.pyplot as plt
def linearna_funkcija(t1, t2):
    if t1!=t2:
        x1,y1=t1
        x2,y2=t2
        m=(y2-y1)/(x2-x1)
        b=(x1*y2-x2*y1)/(x1-x2)
        print("Gradijent je: "+str(m))
        print("Y-odsječak je: "+str(b))
        plt.xlabel("x koordinate")
        plt.ylabel("y koordinate")
        plt.plot([x1,x2],[y1,y2])
    else:
        print("Dvaput ste unijeli istu točku, beskonačno mnogo neodredivih pravaca prolazi kroz ovu točku")

print("Odaberite prikaz slike u prozorčiću s 1, a stvaranje nove slike u pdf formatu sa 2")
odabir=int(input())
if odabir==1:
    linearna_funkcija((4,1),(3,2))
    plt.show()
elif odabir==2:
    naziv=input("Unesite naziv filea ")
    linearna_funkcija((4,1),(3,2))
    plt.savefig(f"{naziv}.pdf")
