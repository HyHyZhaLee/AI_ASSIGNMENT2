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
        best_state = None
        best_Z = -1
        best_path = None

        for _ in range(num_trial):
            current_state = problem.get_initial_state()
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

    def simulated_annealing_search(self, problem: Problem, schedule):
        # TODO 3: simulated_annealing_search
        current = problem.get_initial_state()
        path = [(current.X, current.Y, problem.get_evaluation_value(current))]
        t = 0
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
                # rand = random.uniform(0, 1)
                # print((-1)*deltaE/T)
                if math.exp((-1) * deltaE / T) > random.uniform(0, 1):
                    path.append((next.X, next.Y, next_Z))
                    current = next
            t += 1

    def local_beam_search(self, problem, k):
        # Start with k randomly generated states
        current_states = [problem.get_random_state() for _ in range(k)]
        # Initialize paths for each state
        paths = [[(state.X, state.Y, problem.get_evaluation_value(state))] for state in current_states]

        while True:
            # List to store all successors from all k states
            all_successors = []
            # List to store potential paths corresponding to each successor
            new_paths = []

            # Extend each path with the successors of its last state
            for path in paths:
                last_state_in_path = path[-1]
                last_state_obj = State(last_state_in_path[0], last_state_in_path[1])
                successors = problem.get_successors(last_state_obj)

                for succ in successors:
                    all_successors.append(succ)
                    # Extend the current path with the new successor
                    new_path = path.copy() + [(succ.X, succ.Y, problem.get_evaluation_value(succ))]
                    new_paths.append(new_path)

            # If any successor is a goal state, return the path leading to it
            for path in new_paths:
                last_state_in_path = path[-1]
                last_state_obj = State(last_state_in_path[0], last_state_in_path[1])
                if problem.goal_test(last_state_obj):
                    return path  # Return the path that reached the goal state

            # No goal found yet, select k best successors
            # Sort all successors by their evaluation and select top k
            sorted_indices = sorted(range(len(all_successors)),
                                    key=lambda i: problem.get_evaluation_value(all_successors[i]),
                                    reverse=True)
            paths = [new_paths[i] for i in sorted_indices[:k]]

            # Implement stopping condition (e.g., a max number of iterations or no change in best states)
            # ...

        # If the function reaches this point, it means no goal state was found
        # Return an empty list or None to indicate failure to find a goal state
        return None


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
