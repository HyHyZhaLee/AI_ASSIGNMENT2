from problem import *
import random
import math

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

    def setNext(self, next):
        self.next = next

    def __str__(self):
        return f"({self.state.X},{self.state.Y})"

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial):
        # TODO 2: random_restart_hill_climbing
        searchSpace = problem.get_successors(problem.get_initial_state())
        best_state = None
        best_Z = -1
        best_path = None

        for _ in range(num_trial):
            current_state = random.choice(searchSpace)
            # searchSpace.remove(current_state)
            current_Z = problem.get_evaluation_value(current_state)
            head = Node(current_state)
            current_path = head

            while True:
                neighbors = problem.get_successors(current_state)
                best_neighbor = max(neighbors, key=lambda x: problem.get_evaluation_value(x))
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

        path = [(s.X, s.Y, problem.get_evaluation_value(s)) for s in best_path.getPath()]
        return path
        pass

    def simulated_annealing_search(self, problem: Problem, schedule):
        # TODO 3: simulated_annealing_search
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

    def local_beam_search(self, problem, k):
        states = [problem.get_random_state() for _ in range(k)]
        paths = {state: [(state.X, state.Y, problem.get_evaluation_value(state))] for state in states}
    
        iteration = 0  # Track the number of iterations

        while True:
            print(f"Iteration {iteration}: Current states:")  # Diagnostic print
            for state in states:
                print(f"State {state} with evaluation {problem.get_evaluation_value(state)}")
        
            all_successors = []
            for state in states:
                successors = problem.get_successors(state)
                for succ in successors:
                    if succ not in paths:
                        paths[succ] = paths[state] + [(succ.X, succ.Y, problem.get_evaluation_value(succ))]
                    all_successors.append(succ)
        
            # If no successors were generated, exit the loop
            if not all_successors:
                print("No more successors to explore.")
                break

            all_successors = list(set(all_successors))  # Remove duplicates
            all_successors.sort(key=lambda x: problem.get_evaluation_value(x), reverse=True)
            states = all_successors[:k]

            # If no states have changed (no progress), exit the loop
            if states == all_successors[:k]:
                print("No progress in beam search; terminating.")
                break
        
            iteration += 1  # Increment the iteration count
            # Terminate after a reasonable number of iterations to prevent infinite loop
            if iteration > 1000:  # This is an arbitrary cutoff for the example
                print("Reached iteration limit; terminating.")
                break

        best_state = max(states, key=lambda x: problem.get_evaluation_value(x))
        best_path = paths[best_state]
    
        print("Best path found:", best_path)  # Diagnostic print
        return best_path

if __name__ == "__main__":
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
