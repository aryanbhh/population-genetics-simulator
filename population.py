from individual import Individual
import random

class Population:
    def __init__(self, size, starting_frequency):
        self.individuals = []

        for i in range(size):
            allele1 = "B" if random.random() < starting_frequency else "b"
            allele2 = "B" if random.random() < starting_frequency else "b"
            ind = Individual(allele1, allele2)
            self.individuals.append(ind)

pop = Population(10, 0.7)
print(len(pop.individuals))
print(pop.individuals[0].allele1)