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
            # print(current)
            T = problem.schedule(t)
            if T > 0:
                break
            next = problem.get_random_successor(current)
            deltaE = np.subtract(problem.get_evaluation_value(next), problem.get_evaluation_value(current), dtype=np.int16)
            # print(next.X, next.Y, problem.get_evaluation_value(next) ," - ",current.X, current.Y, problem.get_evaluation_value(current))
            # print(deltaE)
            if deltaE > 0:
                current = next
            else:
                rand = random.uniform(0, 1)
                # print(math.exp(np.divide(deltaE, T)), rand)
                if math.exp(np.divide(deltaE, T)) > rand:
                    current = next
            t += 1

        print(current, problem.get_evaluation_value(current))