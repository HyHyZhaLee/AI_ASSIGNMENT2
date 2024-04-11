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

    def load_state_space(self, filename):
        img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        h, w = img.shape
        X = np.arange(w)
        Y = np.arange(h)
        Z = img
        return X, Y, Z

    def show(self, ax=None):
        # draw state space (surface)
        X, Y = np.meshgrid(self.X, self.Y)
        Z = self.Z
        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection='3d')
        # draw state space (surface)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        plt.show()

    def get_initial_state(self):
        initial_state = State(0, 0)
        return initial_state

    def get_evaluation_value(self, state):
        return self.Z[state.X][state.Y]

    def goal_test(self, state):
        # TODO: return true if state = goal_state
        pass

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

    def get_cost(self, state1, state2):
        return 1

    def heuristic_schedule(self, t):
        pass

    def draw_path(self, path):
        X, Y = np.meshgrid(self.X, self.Y)
        Z = self.Z
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

        # Vẽ đường đi từ danh sách các bộ ba (x, y, z)
        xs = [x for x, y, z in path]
        ys = [y for x, y, z in path]
        zs = [z for x, y, z in path]
        ax.plot(xs, ys, zs, 'r-', zorder=3, linewidth=0.5)  # Dùng 'r-' để vẽ đường màu đỏ

        plt.show()


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
