# TSP_GA_SA
Traveling Salesman Problem solved with Genetic Algorithm and Simulated Annealing

## Problem Statement
There are a set of customers, and a postman. This postman starts from node (0,0), and visits some customers. Suppose there is a path between each pair of nodes. The distance between each pair of two nodes is the Euclidean distance of such two nodes (reserve to 0.01 precision).

Design the shortest path (visiting sequence to customers) for this postman, such that:
* Among customers #5, 10, 15, 20, 25, 30, 35, 40, the postman needs to visit at least three nodes of them. For example, if he visits 5 and 10 and 20 then (15, 25, 30, 35, 40) can be ignored.
* Among customers #2, 4, 6, 8, 10, 20, 22, 32, 33, 35 the postman needs to visit at least five nodes.
* For other customers, each one must be visited.

The locations of each customer are stored in locations.txt. The final result should contain visual representation of the path and the distance.

## Solution
Solutions were obtained by the use of 2 algorithms that are based on natural phenomena, namely Genetic Algorithm (GA_TSP.py) and Simulated Annealing (SA_TSP.py). Simulated Annealing uses a greedy algorithm to obtain an initial path, which is then optimized. To get the solutions run main.py, it will calculate the length of the shortest path, and automatically plot both paths using matplotlib.


## References
Genetic Algorithm:  
https://stackabuse.com/traveling-salesman-problem-with-genetic-algorithms-in-java/  
https://github.com/giacomodeodato/Genetic_Algorithm  
  
Simulated Annealing:  
https://www.theprojectspot.com/tutorial-post/simulated-annealing-algorithm-for-beginners/6  
https://github.com/chncyhn/simulated-annealing-tsp  
