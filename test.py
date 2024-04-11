from search import *
from problem import *

problem = Problem("monalisa.jpg")
search = LocalSearchStrategy()
randomRestartHillClimbing_result = search.random_restart_hill_climbing(problem, 5)
localBeamSearch_result = search.local_beam_search(problem, 5)
simulatedAnnealing_result = search.simulated_annealing_search(problem, problem.schedule)

print("Random restart hill climbing result: ")
print(randomRestartHillClimbing_result)

print("Local beam search result: ")
print(localBeamSearch_result)

print("Simulated Annealing result: ")
print(simulatedAnnealing_result)

problem.draw_path(randomRestartHillClimbing_result, "red")
problem.draw_path(localBeamSearch_result, "blue")
problem.draw_path(simulatedAnnealing_result, "black")
problem.show()


