from simpleai.search import *
import random
from datetime import datetime

class KnapsackProblem(SearchProblem):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.size = len(initial_state)

    def generate_random_state(self):
        # generate a random initial string
        random_state = []
        digits = '01'
        for i in range(number_of_items):
            rand = random.choice(digits)
            random_state.append(rand)
        return random_state

    def _is_valid(self, state):
        '''Check if a state is valid.'''
        # valid states: no more cannibals than missioners on each side,
        # and numbers between 0 and 3
        return (self.weight(state) <= knapsack_capacity)# weight is smaller, it return true()

    def actions(self, state):
        #which element will be chosen ex: 1.index, 2.index...
        actions_list = []
        for i in range(number_of_items):
            if self._is_valid((self.result(state,i))): #self.result returns current state, so weight couldn't calculate the next state.
                actions_list.append(i)
            else:
                continue
        return actions_list

    def result(self, state, action):
        if state[action] == '0':
            state[action] = '1'
        else:
            state[action] = '0'
        return state

    def value(self, state):
        return sum(int(values_of_items[i]) if state[i] == '1' else 0
                       for i in range(len(state)))

    def weight(self, state):
        return sum(int(weights_of_items[i]) if state[i] == '1' else 0
                   for i in range(len(state)))

    def crossover(self, state1, state2):
        # cross both strings, at a random point
        cut_point = random.randint(0, len(state1))
        child = state1[:cut_point] + state2[cut_point:]
        if self._is_valid(self.result(child,i)):
            return child
        else:
            return state1 #we don't know the correct variable to write here, we write state1 to just compile.

    def mutate(self, state):
        #Changes a random element of the permutation array from 0 -> 1 or from 1 -> 0.
        oldstate = state
        r = random.randint(0,len(state)-1)
        if state[r] == 1:
            state[r] = 0
        else:
            state[r] = 1
        if self._is_valid(self.result(state,i)):
            return state
        else:
            return oldstate

def HCS(problem):
    before = datetime.now()
    search = hill_climbing(problem)
    after = datetime.now()
    print("*** Hill Climbing Search ***")
    print("Items selected: ", search.state_representation())
    print("Total profit: ", problem.value(search.state))
    print("Total weight: ", problem.weight(search.state))
    print("Time: ",(after - before).total_seconds())
    print("*"*30)

def HCSRR(problem):
    before = datetime.now()
    search = hill_climbing_random_restarts(problem, restarts_limit=3)
    after = datetime.now()
    print("*** Hill Climbing Random Search ***")
    print("Items selected: ", search.state_representation())
    print("Total profit: ", problem.value(search.state))
    print("Total weight: ", problem.weight(search.state))
    print("Time: ",(after - before).total_seconds())
    print("*"*30)

def GS(problem):
    before = datetime.now()
    search = genetic(problem)
    after = datetime.now()
    print("*** Genetic Search ***")
    print("Items selected: ", search.state_representation())
    print("Total profit: ", problem.value(search.state))
    print("Total weight: ", problem.weight(search.state))
    print("Time: ",(after - before).total_seconds())
    print("*"*30)

def AllAlgorithms(problem):
    print(("*" * 22) + "\n* Local Search Algorithms *\n" + ("*" * 22))
    HCS(problem)
    HCSRR(problem)
    GS(problem)

number_of_items = int(input("Number of items: "))
knapsack_capacity = int(input("Knapsack capacity: "))

weights_of_items = []
print("Weights of items: ")
for i in range(number_of_items):
    weight_by_user = int(input())
    weights_of_items.append(weight_by_user)

values_of_items = []
print("Value of items: ")
for i in range(number_of_items):
    value_by_user = int(input())
    values_of_items.append(value_by_user)

initial_state = []
digits = '01'
for i in range(number_of_items):
    rand = random.choice(digits)
    initial_state.append(rand)
print(initial_state)

knapsack_problem = KnapsackProblem(initial_state)

while True:
    print("Which searching algorithm do you want to calculate?")
    algorithm = int(input("1 - Hill Climbing Search\n"
          "2 - Hill Climbing-Random Restart Search\n"
          "3 - Genetic Search\n"
          "4 - All Algorithms\n"))
    if algorithm == 1:
        HCS(knapsack_problem)
    elif algorithm == 2:
        HCSRR(knapsack_problem)
    elif algorithm == 3:
        GS(knapsack_problem)
    elif algorithm == 4:
        AllAlgorithms(knapsack_problem)
    else:
        print("Invalid input")
        continue
    if input("Exit [e]") =="e":
        break
