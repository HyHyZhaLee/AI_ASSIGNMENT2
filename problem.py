import numpy as np
import matplotlib.pyplot as plt
import cv2

class State:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

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

    def show(self):
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
        #TODO: return true if state = goal_state
        pass

    def get_sucessors(self, state):
        pass

    def get_cost(self):
        pass

    def heuristic_schedule(self, t):
        pass

    def draw_path(self, path):
        # draw a polyline on the surface
        # ax.plot(range(0, 50), range(0, 50), self.Z[range(0, 50), range(0, 50)], 'r-', zorder=3, linewidth=0.5)

        #TODO 1: Visualize all tuples of (x, y, z) and a draw_path(path) function to draw the path on the curved surface
        pass

if __name__ == '__main__':
    # Load pic
    problem = Problem('monalisa.jpg')
    # Test get Z (evaluation_value)
    state = State(0, 0)
    Z = problem.get_evaluation_value(state)
    print(Z)
    # Plot
    problem.show()
