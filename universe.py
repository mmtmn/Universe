import math

class Universe:
    def __init__(self):
        # Define the constants
        self.G = 6.67e-11
        self.c = 2.998e8

        # Define fundamental particles
        self.electron = Particle(9.109e-31, -1.602e-19, (0,0,0))
        self.proton = Particle(1.673e-27, 1.602e-19, (0,0,0))
        self.neutron = Particle(1.675e-27, 0, (0,0,0))

    def gravity(self, m1, m2, r):
        if r <= 0:
            raise ValueError('The distance between the particles must be positive')
        return self.G * ((m1 * m2) / (r ** 2))

    def electromagnetism(self, q1, q2, r):
        if r <= 0:
            raise ValueError('The distance between the particles must be positive')
        return (1/(4*math.pi*8.85e-12)) * (q1*q2) / (r**2)

    def space_time(self, m1, m2, r):
        G = self.G
        c = self.c
        return (1/G) * ((2*math.pi*G*m1*m2)/(c**2)) * math.log(r)
    
    def display_universe_data(self):
        print("Universe Constants:")
        print("G:", self.G)
        print("c:", self.c)
        print("\nFundamental Particles:")
        print("electron:", self.electron.__dict__)
        print("proton:", self.proton.__dict__)
        print("neutron:", self.neutron.__dict__)
        print("\nInteraction Functions:")
        print("Gravity:", self.gravity)
        print("Electromagnetism:", self.electromagnetism)
        print("Space-Time:", self.space_time)

    def display_particles_positions(self):
        print("electron:", self.electron.position)
        print("proton:", self.proton.position)
        print("neutron:", self.neutron.position)

    def update_particles_positions(self, time):
        self.electron.update_position(time)
        self.proton.update_position(time)
        self.neutron.update_position(time)

class Particle:
    def __init__(self, mass, charge, position, velocity=(0,0,0)):
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity

    def update_position(self,time):
        x = self.position[0] + (time * self.velocity[0])
        y = self.position[1] + (time * self.velocity[1])
        z = self.position[2] + (time * self.velocity[2])
        self.position = (x,y,z)

# Create the universe
universe = Universe()

# Display the universe data
universe.display_universe_data()

# Setup 3d library
from vpython import sphere, vector, color

# Create the particles
electron = sphere(pos=vector(*universe.electron.position), radius=0.5, color=color.red)
proton = sphere(pos=vector(*universe.proton.position), radius=0.5, color=color.blue)
neutron = sphere(pos=vector(*universe.neutron.position), radius=0.5, color=color.green)

import time

# Continuously loop
while True:
    # Update particles positions
    universe.update_particles_positions(1)

    # Update particles in 3d library
    electron.pos = vector(*universe.electron.position)
    proton.pos = vector(*universe.proton.position)
    neutron.pos = vector(*universe.neutron.position)

    time.sleep(0.01)
