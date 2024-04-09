from problem import Problem, State
import search

if __name__ == '__main__':
    problem = Problem("./monalisa.jpg")
    path = search.LocalSearchStrategy.simulated_annealing_search(problem=problem, schedule=Problem.schedule)
    # for pos in path:
    #     print(pos)
    # path = [[State(i,j) for i in range(0, 50)] for j in range(0, 50)]
    # print(path)
    # path = []
    # for i in range(0, 50):
    #     # for j in range(0, 50):
    #     path.append(State(i, i))

    # problem.draw_path(path)