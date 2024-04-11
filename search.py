from problem import *
import random

class Node:
    def __init__(self, state):
        self.state = state

class LocalSearchStrategy:
    def random_restart_hill_climbing(self, problem, num_trial):
        #TODO 2: random_restart_hill_climbing
        pass

    def simulated_annealing_search(self, problem, schedule):
        #TODO 3: simulated_annealing_search
        pass

    def local_beam_search(self, problem, k):
        #TODO 4: local_beam_search
        def local_beam_search(self, problem, k):
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
                successors = problem.get_sucessors(node.state)
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
