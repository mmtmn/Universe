# Universe


This code defines a universe by setting the values of several constants, such as the gravitational constant (G) and the speed of light (c), and by defining the fundamental particles of the universe (electron, proton, and neutron), along with their mass and charge. It also defines the laws of physics for this universe, such as the law of gravity and the law of electromagnetism, which can be used to calculate the gravitational and electromagnetic forces between two particles. Finally, the code creates a dictionary called universe that contains all of this information and prints it out.

# Universe version 1

Here are a few ways that this code could be improved:

   1. The code uses a global variable universe to store the properties of the universe. This could lead to naming conflicts if the code is part of a larger program that also uses the variable universe. Instead, the code could define a Universe class and store the properties of the universe as instance variables of that class. This would also make it easier to create multiple universes if needed.


   2. The code defines the laws of physics as standalone functions, but these functions depend on the values of the constants G and c, which are defined outside of the functions. This means that if the values of these constants change, the functions will still use the old values. Instead, the code could define the laws of physics as methods of the Universe class, so that they have access to the current values of the constants.


   3. The code defines the fundamental particles of the universe (electron, proton, and neutron) as dictionaries, but this makes it difficult to work with the particles in a consistent way. For example, the code uses the keys 'mass' and 'charge' to access the mass and charge of a particle, but it is easy to mistype these keys or to forget to use them. Instead, the code could define a Particle class and store the mass and charge of each particle as instance variables of that class. This would make it easier to work with the particles in a consistent and error-free way.


   4. The code does not include any error-checking or validation of the input data. For example, if a user passes a negative value for the distance between two particles to the gravity or electromagnetism functions, the code will still calculate the force, but the result will not be physically meaningful. To prevent this, the code could include checks to ensure that the input data is valid, and raise an error if the data is not valid. This would make the code more robust and prevent it from producing incorrect results.


# Update Universe version 2

In this version of the code, I have defined a Universe class that contains the properties and laws of the universe. I have also defined a Particle class that represents the fundamental particles of the universe. I have then created an instance of the Universe class and printed its properties to verify that it has been created correctly.

# Update Universe version 3

Now you can see it in 3d and run it localy on your own browsers. Some bugs were fixed and some more work needs to be done, but this is a solid start!

# Update Universe

Fixed particles sizes. 

The radius of an electron, proton, and neutron can be found in various physics textbooks, or online sources. For example, the radius of an electron can be found to be approximately 10-15 femtometers (1 femtometer = 10-15 meters). The radius of a proton and neutron can be found to be approximately 0.87 fm and 1.15 fm respectively.
