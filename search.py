from problem import *
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

    def simulated_annealing_search(self, problem, schedule):
        #TODO 3: simulated_annealing_search
        pass

    def local_beam_search(self, problem, k):
        #TODO 4: local_beam_search
        # Start with k random nodes, each with a state
        nodes = [Node(State(random.randint(0, problem.Z.shape[1] - 1),
                            random.randint(0, problem.Z.shape[0] - 1))) for _ in range(k)]
        paths = [[(node.state.X, node.state.Y, problem.get_evaluation_value(node.state))] for node in nodes]

        while True:
            # List to store all successors
            all_successors = []
            paths_new = []

            # Generate successors for all k nodes
            for i, node in enumerate(nodes):
                successors = problem.get_successors(node.state)
                for successor_state in successors:
                    successor_node = Node(successor_state)
                    all_successors.append(successor_node)
                    path = paths[i] + [(successor_state.X, successor_state.Y, problem.get_evaluation_value(successor_state))]
                    paths_new.append(path)

            # If no successors, then no more moves possible
            if not all_successors:
                break

            # Evaluate all successors and sort by evaluation value
            all_successors.sort(key=lambda node: problem.get_evaluation_value(node.state), reverse=True)
            paths_new.sort(key=lambda path: path[-1][2], reverse=True)

            # Select the k best successors
            nodes = all_successors[:k]
            paths = paths_new[:k]

            # Check if reaching a plateau or maximum iteration
            if all(problem.get_evaluation_value(nodes[i].state) <= problem.get_evaluation_value(nodes[0].state) for i in range(1, k)):
                # Return the path for the best state
                return paths[0]
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

    problem.draw_path(randomRestartHillClimbing_result, "red")
    problem.draw_path(localBeamSearch_result, "blue")
    problem.draw_path(simulatedAnnealing_result, "black")
    problem.show()
