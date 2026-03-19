def linearna_funkcija(t1, t2):
    if t1!=t2:
        x1,y1=t1
        x2,y2=t2
        m=(y2-y1)/(x2-x1)
        b=(x1*y2-x2*y1)/(x1-x2)
        print("Gradijent je: "+str(m))
        print("Y-odsječak je: "+str(b))
    else:
        print("Dvaput ste unijeli istu točku, beskonačno mnogo neodredivih pravaca prolazi kroz ovu točku")

linearna_funkcija((3,3),(4,1))