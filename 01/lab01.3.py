from __future__ import division
from vpython import *


# Positioning graph and display window to not block each other
# scene = canvas(x=0, y=0, width=600, height=600)
# graph = graph(x=600, y=0, width=400, height=300)

e = 1.6e-19
oofpez = 9e9 #k

Obslocation = vector(0,0,0)

scalefactor = 50e-9/46.4172

atom1 = sphere(pos = vector(-500e-9,0,0), radius = 10e-9, color = color.red)
atom1.q = 12*e
Earrow = arrow(pos = Obslocation, axis = vector(0,0,0), color = color.cyan)
atom2 = sphere(pos = vector(600e-9,0,0), radius = 10e-9, color = color.yellow)
atom2.q = 5*e
atom3 = sphere(pos = vector(-171.2190437e-9,0,0), radius = 10e-9, color = color.blue)
atom3.q = -e

atom1.pos
Earrow.pos


r1 = Earrow.pos - atom1.pos
r1mag = mag(r1)
r1hat = r1 / r1mag

r2 = Earrow.pos - atom2.pos
r2mag = mag(r2)
r2hat = r2 / r2mag

r3 = Earrow.pos - atom3.pos
r3mag = mag(r3)
r3hat = r3 / r3mag


E1 = oofpez * atom1.q * r1mag**(-2) * r1hat
E2 = oofpez * atom2.q * r2mag**(-2) * r2hat
E3 = oofpez * atom3.q * r3mag**(-2) * r3hat

Enet = E1 + E2 + E3#calculate net magmnetic field
print ("Enet =", Enet,"N/C")

# Earrow.axis = E1 * scalefactor
Earrow.axis = scalefactor * Enet

# print ("The magnitude of E1 field =", mag(E1),"N/C")


#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)