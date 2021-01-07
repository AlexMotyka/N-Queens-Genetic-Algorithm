import random
import numpy as np
import chess
import chess.svg

class Individual(object):
    '''
        This class represents an individual within the population. Each
        indiviudual has a chromosome (which is the postion of the queens on the
        board), as well as a fitness score which is the number of collisions
        the queens have
    '''

    def __init__(self, chromosome, N):
        self.chromosome = chromosome
        self.N = N
        self.fitness = self.calc_fitness()



    def mutate(self):
        # random mutation in the gene
        return random.randint(0, self.N-1)



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
        return Individual(child, self.N)



    def calc_fitness(self):
        '''
            Calculate the fitness score based on the number of collisions.
            Optimal fitness score is 0, and fitness score increases by 1
            with each hit. This function only check for horizontal and diagonal
            hits because we will never have a vertical hit due to the way we
            create chromosomes (a chromosome will at most have one queen per
            column)
        '''
        # initial fitness is perfect 0
        fitness = 0
        # column of current queen
        x1 = 0

        # loop through the queens to check for collisions
        for y1 in self.chromosome:
            # the column of the next queen
            x2 = x1 + 1
            # loop through the remaing queens in the chromosome to check for attacks
            while x2 < self.N:
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
def createChromosome(N):
    chromosome = []
    for i in range(N):
        # random int between 0 and the Chessboard size
        chromosome.append(random.randint(0, N-1))
    return chromosome

def generateBoard(top_chromosome, N):
    board_config = ""
        
    for queen_pos in top_chromosome:
        if int(queen_pos) == (N-1):
            board_config += queen_pos + "Q/"
        elif int(queen_pos) == 0:
            board_config += "Q" + str(N-1) + "/"
        else:
            board_config += queen_pos + "Q" + str((N-1)-int(queen_pos)) + "/"

    board = chess.Board(board_config[:-1])
    svg = chess.svg.board(board, size=350)

    return svg

# TODO: this is where we will receive user input from angular
def evolution(POPULATION_SIZE, N):

    gen = 1
    found_solution = False
    population = []

    # create the initial population
    for i in range(POPULATION_SIZE):
        # random chromosome for each individual
        chromosome = createChromosome(N)
        population.append(Individual(chromosome, N))

    # TODO: While we don't have a soltuion generate and emit the chessboard svg text
    # TODO: Save svg in local file
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

        # generate the a chessboard svg of the top chromosome of the population
        top_chromosome = "".join(str(gene) for gene in population[0].chromosome)
        svg = generateBoard(top_chromosome, N)

        svg_file = open("chess" + str(gen) + ".svg", "w")
        svg_file.write(svg)
        svg_file.close()

        yield svg

        gen += 1

    # TODO: When we have our solution svg emit it and then emit 200 to signal that no more data will be sent
    # print the solution chromosome
    top_chromosome = "".join(str(gene) for gene in population[0].chromosome)
    svg = generateBoard(top_chromosome, N)

    svg_file = open("chess" + str(gen) + ".svg", "w")
    svg_file.write(svg)
    svg_file.close()
    yield svg
