#Simulating the Electric Field of a Uniformly Charged Rod

from __future__ import division
from vpython import *


#-----------Define Constants------------
e      = 1.6e-19             # (Coulombs)    Charge of a proton
oofpez = 9e9                 # (Nm^2 / C^2)  Electric constant
scalefactor = 0.5/619.630133 # (unitless)    Desired magnitude / actual magnitude

L = 2                      # (meters)      The length of the rod
N = 15                     # (unitless)    The number of sections of the rod
Q = 3e-8                   # (Coulombs)    The charge of the rod
deltax = L/N               # (meters)      The length of each segment
deltaq = Q/N               # (Coulombs)    The charge of each segment
# obslocation = vector(0.3,0.4,0)  # (meters) The observation location

N = 100 #makes it looks and act like a line of charge
deltat = 0.001



#----------Set Initial Values----------
x =  -0.5 * L + 0.5 * deltax              # Component of the location of the leftmost piece
Enet = vector(0, 0, 0)                    # The net electric field at obslocation

t = 0 #initial time variable
deltaVtotal = 0 #initial value of total potential difference


#------------Create Objects-------------
while x < L/2 :                           # Loop over the creation of many spheres to be the rod
    sphere(pos = vector(x, 0, 0), radius = 0.1, color = color.cyan) # Make a sphere
    x = x + deltax                        # Loop update

Vgraph = gcurve(color = color.cyan) #create a graph
marker = sphere(pos = vector(0, 0.15, 0), color = color.red, radius = 0.05) #create a marker

marker.v = vector(0.5, 0.5, 0) #redifine the velocity of the marker

#-------------Calculations--------------
while marker.pos.x < 1:
    x =  -0.5 * L + 0.5 * deltax               # Reset for new loop
    Enet = vector(0, 0, 0)                     # Reset for new loop
    while x < L/2 :
        r = marker.pos - vector(x, 0, 0)      # Displacement vector to obslocation
        rmag = mag(r)                          # Magnitude
        rhat = r / rmag                        # Unit vector
        E = (oofpez * deltaq / rmag**2) * rhat # Electric field at obslocation due to current sphere
        Enet = Enet + E                        # Update Enet
        x = x + deltax
        
        rate(10000)
                                 # Loop update

    dl = marker.v * deltat #displacement vector
    deltav = -dot(Enet, dl) #change in potential energy
    deltaVtotal = deltaVtotal + deltav #update total potential energy
    t = t + deltat #update time
    marker.pos = marker.pos + dl #update position

    Vgraph.plot(pos = (t, deltaVtotal)) #create a curve

# print("The total potential energy is: ", deltaVtotal) #print result

marker.v = vector(-0.5, 0, 0)

while marker.pos.x > 0:
    x =  -0.5 * L + 0.5 * deltax               # Reset for new loop
    Enet = vector(0, 0, 0)                     # Reset for new loop
    while x < L/2 :
        r = marker.pos - vector(x, 0, 0)      # Displacement vector to obslocation
        rmag = mag(r)                          # Magnitude
        rhat = r / rmag                        # Unit vector
        E = (oofpez * deltaq / rmag**2) * rhat # Electric field at obslocation due to current sphere
        Enet = Enet + E                        # Update Enet
        x = x + deltax
        
        rate(10000)
                                 # Loop update

    dl = marker.v * deltat #displacement vector
    deltav = -dot(Enet, dl) #change in potential energy
    deltaVtotal = deltaVtotal + deltav #update total potential energy
    t = t + deltat #update time
    marker.pos = marker.pos + dl #update position

    Vgraph.plot(pos = (t, deltaVtotal)) #create a curve

print("The total potential energy is: ", deltaVtotal) #print result

# Earrow = arrow(pos = obslocation, axis = Enet * scalefactor, color = color.orange) # Display arrow

# print "The net E field is: ", Enet, "N/C."  # Print result
# print ("For N =", N, "the magnitude of the total Electric Field is: |Enet|  = ", mag(Enet), "N/C.")


#_______________________________________________________________________________________________
# Keep the window open
while True:
    rate(10)