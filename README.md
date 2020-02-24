# N-Queens Genetic Algorithm

This is a genetic algorithm that finds a solution to the famous N-Queens problem, where N queens have to be placed on an NxN chessboard such that they can not attack eachother. 

## The Chessboard

To represent the position of the queens on the chess board I chose to use an array. The index of the array specifies the column of the queen, and the value at that index represents the row the queen is on. Take for example the array [0, 3, 3, 2]. This array represents a 4x4 chessboard with four queens on it. The first queen is on (column 0, row 0), second queen is on (column 1, row 3), the third is on (column 2, row 3), and the fourth is on (column 3, row 2).

## The Chromosome

In this algorithm a chromosome represents a configuration of queens on the board, whether or not they are conflict with eachother or not. The example array, [0, 3, 3, 2], from above is a chromosome.

## The Individual Class

I created an "Individual" class which consists of a chromosome, a fitness score, and the methods necessary for calculating fitness, mating with another individual, and producing a mutated gene. 

The fitness calculation moves through each queen in the chromosome and checks its position against any queens to the right(This avoids counting the same attack multiple times) to determine if a horizontal or diagonal attack is possible. The function does not check for a vertical collision because each index in the array can have only one queen, therefore a vertical attack is impossible. Everytime an attack can be made the fitness score of that chromosome is increased by 1. A correct solution will have a fitness score of 0 (no possible attacks).

## The Algorithm

