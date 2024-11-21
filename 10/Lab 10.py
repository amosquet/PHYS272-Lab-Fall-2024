#Lab 10
from __future__ import division
from vpython import *


#-----------Define Constants------------
e=1.6e-19
oofpez=9e9


#----------Set Initial Values-----------

B = vector(0, 1, 0)
E = vector(0, .001, 0)
Bscalefactor = 1e-9/mag(B)
Escalefactor = 1e-10

interval = 1e-11
t = 0

#------------Create Objects-------------

atom = sphere(pos = vector(0,0,0), radius = 1e-10, color = color.red)
atom.q = e
atom.m = 7 * 1.7e-27
atom.v = vector(0,0,0)
atom.p = atom.m * atom.v

atomtrail = curve(color = atom.color)

Barrow = arrow(pos = vector(0, 0, -1e-9), axis = B * Bscalefactor)
Earrow = arrow(pos = vector(2e-10, 0, -1e-9), axis = E * Escalefactor)

scene.autoscale = False

#-------------Calculations--------------

while t < interval * 1000000:
    
    F = atom.q * (cross(atom.p/atom.m, B) + E)
    atom.p += F * interval
    atomtrail.append(pos = atom.pos)
    t += interval
    atom.pos += (atom.p / atom.m) * interval
    # atom.v += atom.p / atom.m

#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)
    

    
    
        
    
    


