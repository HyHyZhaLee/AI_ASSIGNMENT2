from problem import State
from problem import Problem
import random

class Node:
    def __init__(self, state):
        self.state = state
        self.next = None

    def getPath(self):
        tmp = self
        path = []
        while tmp != None:
            path += [tmp.state]
            tmp = tmp.next
        return path

    def setNext(self,next):
        self.next = next

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial):
        #TODO 2: random_restart_hill_climbing
        searchSpace = problem.get_sucessors(problem.get_initial_state())
        best_state = None
        best_Z = -1
        best_path = None

        for _ in range(num_trial):
            current_state = random.choice(searchSpace)
            #searchSpace.remove(current_state)
            current_Z = problem.get_evaluation_value(current_state)
            head = Node(current_state)
            current_path = head
            
            while True:
                neighbors = problem.get_sucessors(current_state)
                best_neighbor = max(neighbors,key=lambda x: problem.get_evaluation_value(x))
                best_neighbors_Z = problem.get_evaluation_value(best_neighbor)
                best_Node = Node(best_neighbor)

                if best_neighbors_Z <= current_Z:
                    break
                current_state = best_neighbor
                current_Z = best_neighbors_Z
                current_path.setNext(best_Node)
                current_path = best_Node

            if best_Z < current_Z:
                best_state = current_state
                best_Z = current_Z
                best_path = head

        path = [(s.X,s.Y,problem.get_evaluation_value(s)) for s in best_path.getPath()]
        return path

    def simulated_annealing_search(self, problem, schedule):
        #TODO 3: simulated_annealing_search
        pass

    def local_beam_search(self, problem, k):
        #TODO 4: local_beam_search
        pass