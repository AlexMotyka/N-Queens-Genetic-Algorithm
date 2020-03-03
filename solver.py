import random
import matplotlib.pyplot as plt
import numpy as np

# Number of queens as well as board dimensions(NxN)
N = 8
POPULATION_SIZE = 4000
# Array to store all unique solutions found
solutions = []

# Cumulative generations evolved
total_generations = 1
# Count of unique solutions found
total_solutions = 0
# Generation sizes for histogram
generation_frequencies = []
# Array at index 0 stores a list of total_generations after each evolution process
# Array at index 1 stores a list of total_solutions after each evolution process
cumulative_gen_data = [[],[]]

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
            if probability <= 0.4:
                child.append(gene1)
            elif probability <= 0.8:
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
            create chromosomes (a chromosome will at most have one queen per
            column)
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
            # loop through the remaing queens in the chromosome to check for attacks
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
    global total_solutions
    global total_generations
    global cumulative_gen_data
    global generation_frequencies


    # until we find 92 unique solutions keep evolving to find new solutions
    while len(solutions) < 92:
        new_solution = evolution()
        if new_solution:
            print("Found new solution. Total found: " + str(len(solutions)))
            total_solutions += 1
        else:
            print("Found already existing solution.")

        cumulative_gen_data[0].append(total_generations)
        cumulative_gen_data[1].append(total_solutions)

    for solution in solutions:
        print(solution)

    # create a figure with two subplots
    plt.figure(figsize=(8,5))

    # cumulative generation graph
    plt.subplot(1,2,1)
    plt.plot(cumulative_gen_data[0], cumulative_gen_data[1], 'ro')
    plt.tight_layout(pad=3.0)
    plt.text(20, 92, r'Total Generations: ' + str(cumulative_gen_data[0][-1]))
    plt.grid(True)
    plt.title('# of Generations to Find All Solutions')
    plt.xlabel('# of Generations')
    plt.ylabel('# of Solutions Found')

    # generation frequency histogram
    plt.subplot(1,2,2)
    plt.tight_layout(pad=3.0)
    n, bins, patches = plt.hist(x=generation_frequencies, bins='auto', color='#0504aa', alpha=0.7, rwidth=1)
    plt.grid(axis='y', alpha=0.75)
    plt.grid(True)
    plt.xlabel('# of Generations for Solution')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generation Sizes')
    maxfreq = n.max()
    # Set a clean upper y-axis limit.
    plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

    # display the plots
    plt.show()


def evolution():
    global POPULATION_SIZE
    global solutions
    global total_generations

    gen = 1
    found_solution = False
    population = []

    # create the initial population
    for i in range(POPULATION_SIZE):
        # random chromosome for each individual
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
        # copy them to the next_gen[]
        next_gen.extend(population[:elites])

        # we need to fill the remaining 90% of the next generation with children
        mating_pop = int((90*POPULATION_SIZE)/100)
        for individual in range(mating_pop):
            # select parents from the top 50% of the population for mating
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            # the child is created and added to the next generation
            child = parent1.mate(parent2)
            next_gen.append(child)

        # discard the old pop and replace it with the new gen
        population = next_gen

        # print("Generation: {}\tChromosome: {}\tFitness: {}".format(gen,
        #       "".join(str(gene) for gene in population[0].chromosome),
        #       population[0].fitness))

        gen += 1
        total_generations += 1

    generation_frequencies.append(gen)

    # # print the solution chromosome
    # print("Generation: {}\tChromosome: {}".format(gen,
    #       "".join(str(gene) for gene in population[0].chromosome)))

    # check if the solution is unique
    if population[0].chromosome not in solutions:
        solutions.append(population[0].chromosome)
        return True
    else:
        return False



if __name__ == '__main__':
    main()
