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

    def allele_frequency(self):
        count = 0
        for person in self.individuals:
            if person.allele1 == "B":
                count += 1
            if person.allele2 == "B":
                count+= 1
        return count / (len(self.individuals) * 2)

pop = Population(10, 0.7)
print(pop.allele_frequency())