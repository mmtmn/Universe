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

class Particle:
    def __init__(self, mass, charge):
        self.mass = mass
        self.charge = charge


# Create the universe
universe = Universe()

# Display the universe data
universe.display_universe_data()

# Display the universe
#print(universe.__dict__)
