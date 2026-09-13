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

    def reproduce(self):
        new_generation = []
        for people in range(len(self.individuals)):
            parent_1 = random.choice(self.individuals)
            parent_2 = random.choice(self.individuals)

            allele1 = random.choice([parent_1.allele1, parent_1.allele2])
            allele2 = random.choice([parent_2.allele1, parent_2.allele2])

            child = Individual(allele1, allele2)
            new_generation.append(child)

        self.individuals = new_generation

