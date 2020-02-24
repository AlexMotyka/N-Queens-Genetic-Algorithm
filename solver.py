import random

# Number of queens as well as board dimensions(NxN)
N = 8
POPULATION_SIZE = 50

class Individual(object):
    '''
        This class represents an individual within the population. Each
        indiviudual has a chromosome (which is the postion of the queens on the
        board), as well as a fitness score which is the number of collisions
        the queens have
    '''

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness()

    def mutate(self):
        # random mutation in the gene
        global N
        return random.randint(0, N-1)

    def mate(self, parent2):
        # child chromosome
        child = []
        # create the childs genes
        for gene1, gene2 in zip(self.chromosome, parent2.chromosome):
            probability = random.random()
            # based on probability choose gene from parent1, parent2, or mutate
            if probability < 0.45:
                child.append(gene1)
            elif probability < 0.90:
                child.append(gene2)
            else:
                child.append(self.mutate())
        return Individual(child)

    def calc_fitness(self):
        '''
            Calculate the fitness score based on the number of collisions.
            Optimal fitness score is 0, and fitness score increases by 1
            with each hit. This function only check for horizontal and diagonal
            hits because we will never have a vertical hit due to the way we
            create chromosomes; a chromosome will at most have one queen per
            column.
        '''
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
    population = []

    # create the initial population
    for i in range(POPULATION_SIZE):
        chromosome = createChromosome()
        population.append(Individual(chromosome))

    while not found_solution:
        # sort the population by ascending fitness
        population = sorted(population, key = lambda x:x.fitness)

        # If our best member has a fitness of 0 then we have found a solution
        if population[0].fitness <= 0:
            found_solution = True
            break

        next_gen = []

        # select the "elite" 10% of members of the population to survive to the
        # next generation
        elites = int((10*POPULATION_SIZE)/100)
        next_gen.extend(population[:elites])

        # select the top 50% of the population for mating
        mating_pop = int((50*POPULATION_SIZE)/100)
        for individual in range(mating_pop):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            # the child is created and add to the next generation
            child = parent1.mate(parent2)
            next_gen.append(child)

        population = next_gen

        print("Generation: {}\tChromosome: {}\tFitness: {}".format(gen,
              "".join(str(gene) for gene in population[0].chromosome),
              population[0].fitness))

        gen += 1

    print("SOLUTION Generation: {}\tChromosome: {}\tFitness: {}".format(gen,
          "".join(str(gene) for gene in population[0].chromosome),
          population[0].fitness))



if __name__ == '__main__':
    main()
