from problem import *
import random

class Node:
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return f"({self.state.X},{self.state.Y})"

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial):
        #TODO 2: random_restart_hill_climbing
        pass

    def simulated_annealing_search(self, problem, schedule):
        #TODO 3: simulated_annealing_search
        pass

    def local_beam_search(self, problem, k):
        #TODO 4: local_beam_search
        pass

if __name__ == "__main__":
    problem = Problem("monalisa.jpg")
    search = LocalSearchStrategy()
    randomRestartHillClimbing_result = search.random_restart_hill_climbing(problem, 5)
    localBeamSearch_result = search.local_beam_search(problem, 5)
    simulatedAnnealing_result = search.simulated_annealing_search(problem, problem.heuristic_schedule)

    print("Random restart hill climbing result: ")
    print(randomRestartHillClimbing_result)

    print("Local beam search result: ")
    print(localBeamSearch_result)

    print("Simulated Annealing result: ")
    print(simulatedAnnealing_result)


