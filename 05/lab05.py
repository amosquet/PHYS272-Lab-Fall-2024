from __future__ import division
from vpython import *

#define constants
e = 1.6e-19
oofpez = 9e9
scalefactor = 1e-10/0.0004217950613831132

muzofp = 1e-7
deltat = 5e-20

#initial values
t = 0

#create objects
atom = sphere(pos = vector(2e-9, 0, 0), radius = 1e-10, color = color.red)
atom.q = 1.6e-19 #charge
atom.v = vector(-4e5, 0, 0) #m/s

Barrow = arrow(pos = vector(0, 0, -6e-10), axis = vector(0, 0, 0), color = color.green)

scene.autoscale = 0

obs1 = arrow(pos = vector(0, 0, 6e-10), axis = vector(0,0,0), color = color.yellow)
obs2 = arrow(pos = vector(0, 6e-10, 0), axis = vector(0,0,0), color = color.yellow)
obs3 = arrow(pos = vector(0, -6e-10, 0), axis = vector(0,0,0), color = color.yellow)

#calculations
# while atom.pos.x > -2e-9:
#     r = Barrow.pos - atom.pos
#     rmag = mag(r)
#     rhat = r / rmag
#     B = (muzofp * atom.q * cross(atom.v, rhat) / (rmag**2))
#     Barrow.axis = B * scalefactor

#     r1 = obs1.pos - atom.pos
#     rmag1 = mag(r1)
#     rhat1 = r1 / rmag1
#     B1 = (muzofp * atom.q * cross(atom.v, rhat1) / (rmag1**2))
#     obs1.axis = B1 * scalefactor

#     r2 = obs2.pos - atom.pos
#     rmag2 = mag(r2)
#     rhat2 = r2 / rmag2
#     B2 = (muzofp * atom.q * cross(atom.v, rhat2) / (rmag2**2))
#     obs2.axis = B2 * scalefactor

#     r3 = obs3.pos - atom.pos
#     rmag3 = mag(r3)
#     rhat3 = r3 / rmag3
#     B3 = (muzofp * atom.q * cross(atom.v, rhat3) / (rmag3**2))
#     obs3.axis = B3 * scalefactor

#     atom.pos = atom.pos + atom.v * deltat

            
#     rate(10000)

# print(mag(B))

scalefactor = 1e-10/0.1662768775266122
obsA = arrow(pos = vector( 5e-10,0,0), axis=vector(0,0,0), color = color.purple)
atom.v = vector(3e6*cos(60*(2*pi/180)), 3e6*sin(60*(2*pi/180)), 0)
atom.pos = vector(0,0,0)
atom.q = atom.q * -1

r4 = obsA.pos - atom.pos
rmag4 = mag(r4)
rhat4 = r4 / rmag4
B4 = (muzofp * atom.q * cross(atom.v, rhat4) / (rmag4**2))
obsA.axis = B4 * scalefactor
print(B4)
print(mag(B4))

E = 9e9 * atom.q / (mag(r4)**2) * rhat4
print(E)
Earrow = arrow(pos = obsA.pos, axis = E * 1e-10/mag(E), color = color.orange)





#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)

