import random

N = 8
POPULATION_SIZE = 50

class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    # calculate the fitness score which is the number of queen conflicts
    def calc_fitness(self):
        fitness = 0
        return fitness

# create a chromosome with random genes
def createChromosome():
    global N
    chromosome = []
    for i in range(N):
        # random int between 0 and the Chessboard size
        chromosome.append(random.randint(0, N-1))
    return chromosome

def main():
    global POPULATION_SIZE

    gen = 1
    found_solution = False
    # array of Individuals
    population = []

    for i in range(POPULATION_SIZE):
        chromosome = createChromosome()
        population.append(Individual(chromosome))

    print(population.chromosome)

if __name__ == '__main__':
    main()
