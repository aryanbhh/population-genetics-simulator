from population import Population

pop = Population(100, 0.7)
frequencies = []

frequencies.append(pop.allele_frequency())

for generations in range(50):
    pop.reproduce()
    frequencies.append(pop.allele_frequency())

print(frequencies)
