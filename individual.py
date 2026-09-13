class Individual:
    def __init__(self, allele1, allele2):
        self.allele1 = allele1
        self.allele2 = allele2

if __name__ == "__main__":
    ind = Individual("B", "b")
    print(ind.allele1) 
    print("hello world")