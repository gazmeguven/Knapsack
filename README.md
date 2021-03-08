## Knapsack Problem with AI

*Formulated and developed a solution to the problem by applying several local search algorithms: Hill Climbing Search, Hill Climbing with Random Restarts, and Genetic Algorithm.

**0-1 Knapsackproblem:** This famous problem is usually stated as follows: Given a set of items, each with a weight and a value, determine which items to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. It is not possible to take a portion of an item, we can either decide to take it or not.

1. simpleai library is used.
2. The program has a simple console-based menu which takes the following inputs from the user: number of items, knapsack capacity, weights of each item, and values of each item.
3. The  problem is defined as a search problem (implemented required functions actions, result, value, crossover, mutate, generate_random_state) and called local search algorithms (hill_climbing, hill_climbing_random_restarts, and genetic) to solve the problem.
4. The program output shows the result including the list of items selected, total profit of the selected items, and total weight of the selected items.
