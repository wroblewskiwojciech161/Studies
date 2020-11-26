import random
import time
import sys

"""Wojciech Wroblewski lista 3 zad 1  amh particle swarm optimization """

in_data = input().split()

t = int(in_data[0])

vector = []

vector.append(int(in_data[1]))
vector.append(int(in_data[2]))
vector.append(int(in_data[3]))
vector.append(int(in_data[4]))
vector.append(int(in_data[5]))

epsilons = []

epsilons.append(float(in_data[6]))
epsilons.append(float(in_data[7]))
epsilons.append(float(in_data[8]))
epsilons.append(float(in_data[9]))
epsilons.append(float(in_data[10]))

"""print(vector)
print(epsilons)
print(t)
"""


def function(vector, epsilons):
    sum = 0
    for i in range(0, len(vector)):
        sum += epsilons[i] * (abs(vector[i]) ** (i + 1))
    return sum


"""reprezentacja czastki"""


class Particle:
    def __init__(self, base_vector, n_vars, lower, upper):
        self.base_vector = base_vector
        self.nvars = n_vars
        self.position = self.get_particle_vector()
        self.best_position = self.position
        self.value = function(self.position, epsilons)
        self.local_best = function(self.position, epsilons)
        self.lower = lower
        self.upper = upper
        self.velocity = []

        for i in range(0, self.nvars):
            self.velocity.append(random.uniform(-1, 1))

    """storz wektor pozycji na podstawie wektora bazowego i zakresu"""

    def get_particle_vector(self):
        vector = []
        for i in range(0, len(self.base_vector)):
            number = self.base_vector[i] + random.uniform(-50, 50)
            vector.append(number)

        return vector

    def update_velocity(self, global_best_position):
        w = 0.6  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range(0, self.nvars):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.best_position[i] - self.position[i])
            vel_social = c2 * r2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = w * self.velocity[i] + vel_cognitive + vel_social

    def update_position(self):
        for i in range(0, self.nvars):
            self.position[i] = self.position[i] + self.velocity[i]


"""klasa implementujaca PSO"""


class PSO():
    def __init__(self, base_vector, nvars, number_of_particles, lower, upper):
        self.number_of_particles = number_of_particles
        self.lower = lower
        self.upper = upper
        self.base_vector = base_vector
        self.nvars = nvars
        self.global_best_value = None
        self.global_best_position = None

    """tworzenie roju poczatkowego"""

    def create_swarm(self):
        swarm = []
        for i in range(0, self.number_of_particles):
            p = Particle(self.base_vector, self.nvars, self.lower, self.upper)
            swarm.append(p)
        return swarm

    """PSO """

    def calculation(self):
        swarm = self.create_swarm().copy()
        self.global_best_position = self.base_vector
        self.global_best_value = function(self.base_vector, epsilons)

        t_end = time.time() + t
        while time.time() < t_end:

            for p in range(0, self.number_of_particles):
                # update wartosci
                swarm[p].value = function(swarm[p].position, epsilons)

                # update lokalny
                if swarm[p].value < swarm[p].local_best:
                    swarm[p].local_best = swarm[p].value
                    swarm[p].best_position = swarm[p].position.copy()

                # update globalny

                if swarm[p].value < self.global_best_value:
                    self.global_best_value = swarm[p].value
                    self.global_best_position = swarm[p].position.copy()

            # update predkosci i pozycji
            for j in range(0, self.number_of_particles):
                swarm[j].update_velocity(self.global_best_position)
                swarm[j].update_position()

        for i in range(0, len(self.global_best_position)):
            sys.stdout.write(str(self.global_best_position[i]) + "  ")
        sys.stdout.write(str(self.global_best_value) + " ")


nvars = len(vector)
lower = -50
upper = 50

pso = PSO(vector, nvars, 10, lower, upper)
pso.calculation()

