import math

mass=0
minWidth=50

outfile = open("masspoints.txt", "w")
while mass<8000:
    outfile.write(str(mass)+", ")
    if mass*0.1 > minWidth:
        mass=mass*1.1
    else:
        mass += minWidth
    div=25
    if (mass>=1000 and mass < 2000): div=50
    elif (mass>=2000 and mass < 3000): div=100
    elif (mass>3000): div=200
    mass=round(mass/div,0)*div
outfile.close()
