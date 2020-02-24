import random

N = 4
POPULATION_SIZE = 1

class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    # calculate the fitness score which is the number of queen conflicts
    def calc_fitness(self):
        global N
        # initial fitness is perfect 0
        fitness = 0
        # column of current queen
        x1 = 0

        # loop through the queens to check for collisions
        for y1 in self.chromosome:
            # the column of the next queen
            x2 = x1 + 1
            # loop through the remaing queens in the chromosome
            while x2 < N:
                # the row value at index x2
                y2 = self.chromosome[x2]
                # check for horizontal collision (same row)
                if y1 == y2:
                    fitness += 1
                # check for diagonal collision by comparing magnitudes
                elif abs(x1 - x2) == abs(y1-y2):
                    fitness += 1
                x2 += 1
            x1 += 1
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

    print(population[0].chromosome)
    print(population[0].fitness)

if __name__ == '__main__':
    main()
