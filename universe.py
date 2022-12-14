import os
import math

# Create the universe

# Define the constants
G = 6.67e-11
c = 2.998e8

# Define fundamental particles
electron = {'mass': 9.109e-31, 'charge': -1.602e-19}
proton = {'mass': 1.673e-27, 'charge': 1.602e-19}
neutron = {'mass': 1.675e-27, 'charge': 0}

# Define the laws of physics
def gravity(m1, m2, r):
    return G * ((m1 * m2) / (r ** 2))

def electromagnetism(q1, q2, r):
    return (1/(4*math.pi*8.85e-12)) * (q1*q2) / (r**2)

# Create the universe
universe = {}
universe['constants'] = {'G': G, 'c': c}
universe['fundamental_particles'] = [electron, proton, neutron]
universe['laws'] = {'gravity': gravity, 'electromagnetism': electromagnetism}

# Display the universe
print(universe)