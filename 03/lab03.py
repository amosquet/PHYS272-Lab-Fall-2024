from __future__ import division
from vpython import *

# Positioning graph and display window to not block each other
# scene = canvas(x=0, y=0, width=600, height=600)
# graph = graph(x=600, y=0, width=400, height=300)


#define constants
e = 1.6e-19
oofpez = 9e9
scalefactor = 0.5/16384.961849456373 #adjust denominator to scale arrows using Enet magnitude


#initial values
L = 2 #length of rod in meters
N = 15 #number of sections of the rod
Q = 3e-8 #total charge on the rod
deltax = L / N #length of each segment in terms of L and N
deltaq =  Q / N #charge of each section in tersm of N and Q
obslocation = vector(0.3,0.4,0) #observation location in meters
x = (-L/2 + deltax/2)
Enet = vector(0,0,0)


#calculations
while x < L/2:
    sphere(pos=vector(x,0,0), radius = 0.1, color = color.cyan)
    x = x + deltax
    
for i in range(6):

    x = (-L/2 + deltax/2)
    Enet = vector(0,0,0)

    while x < L/2:
            
        E = oofpez * (deltaq/mag(obslocation - vector(x,0,0))**2) * norm(obslocation - vector(x,0,0))
        Enet = Enet + E
        x = x + deltax
        
    Earrow = arrow(pos = obslocation, axis = scalefactor * Enet, color = color.red)
    i = i + 1
    obslocation = obslocation + vector(0.2,-0.2,0)

print(Enet)
print(mag(Enet))



#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)