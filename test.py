from problem import Problem, State
from search import LocalSearchStrategy
import numpy as np

if __name__ == '__main__':
    problem = Problem("./monalisa.jpg")
    path = LocalSearchStrategy.simulated_annealing_search(problem=problem, schedule=problem.schedule)
    # path = LocalSearchStrategy().random_restart_hill_climbing(problem, 500)


    # for pos in path:
    #     print(pos)
    # path = [[State(i,j) for i in range(0, 50)] for j in range(0, 50)]
    print(path)
    # print(max(path, key=lambda item: item[2]))
    # path = []
    # for i in range(0, 50):
    #     # for j in range(0, 50):
    #     path.append(State(i, i))

    problem.draw_path(path)