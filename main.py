from population import Population
import matplotlib.pyplot as plt

pop = Population(100, 0.7)
frequencies = []

frequencies.append(pop.allele_frequency())

for generations in range(50):
    pop.reproduce()
    frequencies.append(pop.allele_frequency())

print(frequencies)

plt.plot(frequencies)
plt.xlabel("Generation")
plt.ylabel("Allele Frequency (B)")
plt.title("Genetic Drift Over Generations")
plt.show()