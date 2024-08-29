from __future__ import division
from vpython import *

# Positioning graph and display window to not block each other
scene = canvas(x=0, y=0, width=600, height=600)
graph = graph(x=600, y=0, width=400, height=300)

# Define Constants
e = 1.6e-19
oofpez = 9e9

# Set Initial Values

# Create Objects
atom = sphere(pos=vector(-10e-10, 0, 0), radius=1e-10, color=color.red)
atom.q = 10 * e
Earrow = arrow(pos=vector(0, 5e-10, 0), axis=vector(0, 0, 0), color=color.orange)

Egraph = gcurve(color=color.cyan)

scene.autoscale=0

while atom.pos.x < 1e-9:
    # Calculations

    r = Earrow.pos - atom.pos
    rmag = mag(r)
    rhat = r / rmag
    E = oofpez * (atom.q / rmag**2) * rhat

    # print ("E =", E, "N/C")

    Earrow.axis = E

    scalefactor = 8.68e-21
    Earrow.axis = scalefactor * E


    t = 0
    deltat = 1e-13
    atom.v = vector(1,0,0)

    atom.pos=atom.pos+deltat*atom.v
    Egraph.plot(pos=(rmag,mag(E)))
    t=t+deltat


# Keep the window open
while True:
    rate(10)