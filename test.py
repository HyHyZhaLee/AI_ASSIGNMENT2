from search import LocalSearchStrategy
from problem import Problem
from problem import State

if __name__ == '__main__':
    # Load pic
    problem = Problem('monalisa.jpg')
    searchMethod = LocalSearchStrategy()
    rrhc_path = searchMethod.random_restart_hill_climbing(problem, 3)
    problem.draw_path(rrhc_path)
    # Plot
    problem.show()


