import random, math
from scipy.spatial.distance import euclidean as eu
from Data import dataPreProcess

class SA():
    def __init__(self, coords):
        self.coords = coords
        self.N = len(self.coords)
        self.all_locs = [i for i in range(self.N)]

        self.T = math.sqrt(self.N)
        self.alpha = 0.995
        self.stopping_temperature = 1e-8

        self.best_path = None
        self.best_fit = float("inf")

    def dist(self, loc1, loc2):
        """ Euclidean distance between two locations. """
        return eu(self.coords[loc1], self.coords[loc2])

    def fitness(self, path):
        """ Fitness value (total distance) of the path. """
        fit = 0
        for i in range(self.N):
            fit += self.dist(path[i % self.N], path[(i + 1) % self.N])
        return fit

    def greedy(self):
        """ Greedy algorithm to obtain an initial path. """
        visit_loc = random.choice(self.all_locs)
        path = [visit_loc]
        unvisit_loc = set(self.all_locs)
        unvisit_loc.remove(visit_loc)

        while unvisit_loc:
            next_loc = min(unvisit_loc, key=lambda x: self.dist(visit_loc, x))
            unvisit_loc.remove(next_loc)
            path.append(next_loc)
            visit_loc = next_loc

        return path, self.fitness(path)

    def accept(self, candidate):
        """ Accept if candidate is better than current, else leave it to chance. """
        candidate_fitness = self.fitness(candidate)
        if candidate_fitness < self.fit:
            self.fit, self.path = candidate_fitness, candidate
            if candidate_fitness < self.best_fit:
                self.best_fit, self.best_path = candidate_fitness, candidate
        else:
            if random.random() < math.exp(-abs(candidate_fitness - self.fit) / self.T):
                self.fit, self.path = candidate_fitness, candidate

    def sim_anneal(self, plotPath=False):
        """ Execute simulated annealing algorithm. """
        self.path, self.fit = self.greedy()

        while self.T >= self.stopping_temperature:
            candidate = list(self.path)
            l = random.randint(2, self.N - 1)
            i = random.randint(0, self.N - l)
            candidate[i:(i+l)] = reversed(candidate[i:(i+l)])
            self.accept(candidate)
            self.T *= self.alpha

        # end path where it started
        self.best_path.append(self.best_path[0])

        if plotPath == True:
            dataPreProcess().plotPath(self.coords, self.best_path, self.N)

        return (self.best_path, self.best_fit)


if __name__ == "__main__":
    coords = dataPreProcess().getLocs()
    gr_path, gr_fit = SA(coords).greedy()
    sa_path, sa_fit = SA(coords).sim_anneal()
    print("Results of the greedy algorithm:")
    print("Path:\n{0}\nTotal distance: {1:.2f}".format(gr_path, gr_fit))
    print("\n")
    print("Results of the simulated annealing:")
    print("Path:\n{0}\nTotal distance: {1:.2f}".format(sa_path, sa_fit))
