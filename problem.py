import numpy as np
import matplotlib.pyplot as plt
import cv2
import random


class State:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __str__(self):
        return f"({self.X},{self.Y})"


class Problem:
    def __init__(self, filename):
        self.X, self.Y, self.Z = self.load_state_space(filename)
        X, Y = np.meshgrid(self.X, self.Y)
        Z = self.Z
        fig = plt.figure(figsize=(8, 6))
        self.ax = plt.axes(projection='3d')
        self.ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z = img
        return X, Y, Z

    def show(self):
        # draw state space (surface)
        plt.show()
        pass

    def get_random_state(self):
        random_index_x = random.randint(0, self.Z.shape[1] - 1)  # Width
        random_index_y = random.randint(0, self.Z.shape[0] - 1)  # Height
        return State(random_index_x, random_index_y)

    def get_initial_state(self):
        # Get random initial state
        initial_state = self.get_random_state()
        return initial_state

    def get_evaluation_value(self, state):
        # Make sure you are accessing the Z matrix within its bounds
        if 0 <= state.X < self.Z.shape[1] and 0 <= state.Y < self.Z.shape[0]:
            return self.Z[state.Y][state.X]
        else:
            raise ValueError(f"State coordinates out of bounds: X={state.X}, Y={state.Y}")

    def goal_test(self, state):
        # Example: Goal is to find the highest intensity value.
        # Modify according to your goal criteria.
        goal_state = np.max(self.Z)
        return (self.get_evaluation_value(state) == goal_state)

    def get_successors(self, state):
        successors = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                      (1, 1)]  # Include diagonal directions
        min_x, max_x = min(self.X), max(self.X)
        min_y, max_y = min(self.Y), max(self.Y)

        for dx, dy in directions:
            newX, newY = state.X + dx, state.Y + dy
            if min_x <= newX <= max_x and min_y <= newY <= max_y:  # Check against actual min and max values
                successors.append(State(newX, newY))
        return successors

    def get_random_successor(self, state):
        successors = self.get_successors(state)
        if successors:
            return random.choice(successors)
        else:
            return None

    def get_cost(self, path):
        if path: return len(path)
        return 0
    def get_last_value(self, path):
        if path: return path[len(path)-1][2]

    def schedule(self, t, initial_temp=100, cooling_rate=0.95):
        return initial_temp * (cooling_rate ** t)

    def draw_path(self, path, color='red'):
        if path:
            X_array = []
            Y_array = []
            Z_array = []
            for state in path:
                X_array.append(state[0])
                Y_array.append(state[1])
                Z_array.append(state[2])

            self.ax.plot(X_array, Y_array, Z_array, color, zorder=3, linewidth=0.5)


if __name__ == '__main__':
    # Load pic
    problem = Problem('monalisa.jpg')
    initialState = State(0, 0)

    # Test print get Z state(0,0)
    print("Test getting z at initial state (0,0): ")
    print(problem.get_evaluation_value(initialState))
    # Test getSuccesor
    print("Test getting z at initial state (0,0): ")
    initialState_successor = problem.get_successors(initialState)
    for successor in initialState_successor:
        print(successor)
    # Plot
    problem.show()
