import math

class Universe:
    def __init__(self):
        # Define the constants
        self.G = 6.67e-11
        self.c = 2.998e8

        # Define fundamental particles
        self.electron = Particle(9.109e-31, -1.602e-19)
        self.proton = Particle(1.673e-27, 1.602e-19)
        self.neutron = Particle(1.675e-27, 0)

    def gravity(self, m1, m2, r):
        if r <= 0:
            raise ValueError('The distance between the particles must be positive')
        return self.G * ((m1 * m2) / (r ** 2))

    def electromagnetism(self, q1, q2, r):
        if r <= 0:
            raise ValueError('The distance between the particles must be positive')
        return (1/(4*math.pi*8.85e-12)) * (q1*q2) / (r**2)


class Particle:
    def __init__(self, mass, charge):
        self.mass = mass
        self.charge = charge


# Create the universe
universe = Universe()

# Display the universe
print(universe.__dict__)
