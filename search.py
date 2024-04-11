from problem import Problem
import math
import random
import numpy as np

class LocalSearchStrategy:
    def simulated_annealing_search(problem: Problem, schedule):
        current = problem.get_initial_state()
        path = [(current.X, current.Y, problem.get_evaluation_value(current))]
        t = 1
        while True:
            T = math.floor(schedule(t))
            if T == 0:
                path.append((current.X, current.Y, problem.get_evaluation_value(current)))
                return path
            next = problem.get_random_successor(current)
            # print(next)
            next_Z = problem.get_evaluation_value(next)
            while (next.X, next.Y, next_Z) in path:
                next = problem.get_random_successor(current)

            deltaE = np.subtract(problem.get_evaluation_value(next), next_Z, dtype=np.int16)
            
            if deltaE > 0:
                path.append((next.X, next.Y, next_Z))
                current = next
            else:
                rand = random.uniform(0, 1)
                if math.exp(np.divide(deltaE, T)) > rand:
                    path.append((next.X, next.Y, next_Z))
                    current = next
            t += 1
