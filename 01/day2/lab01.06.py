from __future__ import division
from vpython import *


# Positioning graph and display window to not block each other
# scene = canvas(x=0, y=0, width=600, height=600)
# graph = graph(x=600, y=0, width=400, height=300)

e = 1.6e-19
oofpez = 9e9 #k

Obslocation = vector(1.8e-9,1e-9,0)

scalefactor = 5e-10/2.14355e+08

atom1 = sphere(pos = vector(0.5e-9,0,0), radius = 1e-10, color = color.blue)
atom1.q = -e
atom2 = sphere(pos = vector(-0.5e-9,0,0), radius = 1e-10, color = color.red)
atom2.q = e

# atom1.pos
# Earrow.pos


r1 = Obslocation - atom1._pos
r1mag = mag(r1)
r1hat = r1 / r1mag

r2 = Obslocation - atom2.pos
r2mag = mag(r2)
r2hat = r2 / r2mag


E1 = oofpez * atom1.q * r1mag**(-2) * r1hat
E2 = oofpez * atom2.q * r2mag**(-2) * r2hat

Enet = E1 + E2 #calculate net magmnetic field
print ("Enet =", Enet,"N/C")


Earrow = arrow(pos = Obslocation, axis = Enet * scalefactor, color = color.orange)


print ("The magnitude of E1 field =", mag(E1),"N/C")


#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)