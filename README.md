# N-Queens Genetic Algorithm

This is a genetic algorithm that finds a solution to the famous N-Queens problem, where N queens have to be placed on an NxN chessboard such that they can not attack eachother. Currently the algorithm continues the evolution process until all 92 possible solutions for N=8 have been discovered.

## The Chessboard

To represent the position of the queens on the chess board I chose to use an array. The index of the array specifies the column of the queen, and the value at that index represents the row the queen is on. Take for example the array [2,7,3,0,5,1,4,6]. This array represents an 8x8 chessboard with 8 queens on it (visualized using the bottom left board). The first queen is found on (column 0, row 2) and visualized on the chessboard by (columan a, row 3). The second queen is on (column 1, row 7) and visualized on the chessboard by (column b, row 8). This continues so on so forth for each queen. The board on the bottom right represents a solved board where no queen attakc are possible.

![Image of unsolved board](https://github.com/AlexMotyka/N-Queens-Genetic-Algorithm/blob/master/evolution_svgs/chess1.svg)
![Image of solved board](https://github.com/AlexMotyka/N-Queens-Genetic-Algorithm/blob/master/evolution_svgs/chess6.svg)

## The Chromosome

In this algorithm a chromosome represents a configuration of queens on the board, whether or not they are in conflict with eachother. The array [2,7,3,0,5,1,4,6] from above is a an example of a chromosome. Each value in the array is a 'gene' that makes up the chromosome.

## The Individual Class

I created an "Individual" class which consists of a chromosome, a fitness score, and the methods necessary for calculating fitness, mating with another individual, and producing a mutated gene. 

The fitness calculation moves through each queen in the chromosome and checks its position against any queens to the right) to determine if a horizontal or diagonal attack is possible. Only checking against queens to the right avoids counting the same attack multiple times. 

The function does not check for a vertical collision because each index in the 1-dimensional array can have only one queen, therefore a vertical attack is impossible. Everytime an attack can be made the fitness score of that chromosome is increased by 1. A correct solution will have a fitness score of 0 (no possible attacks).

## The Algorithm

### Initialize
- First an N value, and population size is specified. 
- Next the initial population is created and stored in an array. The population members will be instances of the Individual class with randomly generated chromosomes

### Evolution
- Until we find a member with a fitness of 0 we will execute the evolution process
- Sort the population in ascending order of fitness (From fittest to least fit)
- Check if the fittest member has a fitness score of 0. If it does stop the evolution and print the result, else continue.
- Create an array for the next generation. This generation will have the exact same size as the current population.
#### Selection
- Select the top 10% of the current population. These are the elite who survive and are will continue into the next generation.

#### Crossover & Mutation
- Take the top 50% of the population and let them mate to fill up the remaining 90% of the next generation population with children. When the children's chromosomes are created each gene has a a 45% chance to be parent 1's gene, a 45% chance to be parent 2's gene, and a 10% chance to be a randomly mutated gene.
- Destroy the old population, the new generation now becomes the current population and the evolution cycle happens again.

## Result

The below gif shows the evolution process that transformed the top left board into the solution board on the right.

![Image of evolution process](https://github.com/AlexMotyka/N-Queens-Genetic-Algorithm/blob/master/Evolution.gif)


