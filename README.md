# N-Queens Genetic Algorithm

This is a genetic algorithm that finds a solution to the famous N-Queens problem, where N queens have to be placed on an NxN chessboard such that they can not attack eachother. 

## The Chessboard

To represent the position of the queens on the chess board I chose to use an array. The index of the array specifies the column of the queen, and the value at that index represents the row the queen is on. Take for example the array [0, 3, 3, 2]. This array represents a 4x4 chessboard with four queens on it. The first queen is on (column 0, row 0), second queen is on (column 1, row 3), the third is on (column 2, row 3), and the fourth is on (column 3, row 2).

## The Chromosome

In this algorithm a chromosome represents a configuration of queens on the board, whether or not they are conflict with eachother or not. The example array [0, 3, 3, 2] from above is a chromosome. Each value in the array is a 'gene' in the chromosome.

## The Individual Class

I created an "Individual" class which consists of a chromosome, a fitness score, and the methods necessary for calculating fitness, mating with another individual, and producing a mutated gene. 

The fitness calculation moves through each queen in the chromosome and checks its position against any queens to the right(This avoids counting the same attack multiple times) to determine if a horizontal or diagonal attack is possible. The function does not check for a vertical collision because each index in the array can have only one queen, therefore a vertical attack is impossible. Everytime an attack can be made the fitness score of that chromosome is increased by 1. A correct solution will have a fitness score of 0 (no possible attacks).

## The Algorithm

#### Initialize
- First an N value, and population size is specified. 
- Next the initial population is created and stored in an array. The population members will be instances of the Individual class with randomly generated chromosomes

#### Evolution
- Until we find a member with a fitness of 0 we will execute the evolution process
- Sort the population in ascending order of fitness (From fittest to least fit)
- Check if the fittest member has a fitness score of 0. If it does stop the evolution and print the result, else continue.
- Create an array for the next generation. This generation will have the exact same size as the current population.
- Select the top 10% of the cureent population. These are the elite who survive and are will continue into the next generation.

#### Crossover & Mutation
- Take the top 50% of the population and let them mate to fill up the remaining 90% of the next generation population with children. When the children's chromosomes are created each gene has a a 45% chance to be parent 1's gene, a 45% chance to be parent 2's gene, and a 10% chance to be a randomly mutated gene

