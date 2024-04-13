import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

class State:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __str__(self):
        return "(" + str(self.X) + ", " + str(self.Y) + ")"

class Problem:
    def __init__(self, filename):
        self.X, self.Y, self.Z = self.load_state_space(filename)
        print(self.Z)

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
        X, Y = np.meshgrid(self.X, self.Y)
        Z = self.Z
        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection='3d')
        # draw state space (surface)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        plt.show()

    def get_initial_state(self) -> State:
        return State(0,0)

    def get_evaluation_value(self, state: State):
        return self.Z[state.Y][state.X]

    def goal_test(self, state: State):
        #TODO: return true if state = goal_state
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

    def get_random_successor(self, state: State) -> State:
        randomNumber = random.randint(0, 7)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                      (1, 1)]
        min_x, max_x = min(self.X), max(self.X)
        min_y, max_y = min(self.Y), max(self.Y)
        dx, dy = directions[randomNumber]

        newX, newY = state.X + dx, state.Y + dy
        if min_x <= newX <= max_x and min_y <= newY <= max_y:
            return State(newX, newY)
        return self.get_random_successor(state)

    def get_cost(self):
        pass

    def heuristic_schedule(self, t):
        pass

    def draw_path(self, path):
        # draw a polyline on the surface
        # ax.plot(range(0, 50), range(0, 50), self.Z[range(0, 50), range(0, 50)], 'r-', zorder=3, linewidth=0.5)

        #TODO 1: Visualize all tuples of (x, y, z) and a draw_path(path) function to draw the path on the curved surface
        X, Y = np.meshgrid(self.X, self.Y)

        fig = plt.figure(figsize=(8,6))
        ax = plt.axes(projection='3d')
        # draw state space (surface)
        ax.plot_surface(X, Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        # draw a polyline on the surface\
        X_array = []
        Y_array = []
        Z_array = []

        for state in path:
            X_array.append(state[0])
            Y_array.append(state[1])
            Z_array.append(state[2])
        
        ax.plot(X_array, Y_array, self.Z[Y_array, X_array], 'r-', zorder=3, linewidth=0.5)
        plt.show()

    def schedule(self, t):
        # print(np.max(self.Z))
        return np.max(self.Z) * (0.95**t)