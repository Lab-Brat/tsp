import math, random, random, copy
from Data import dataPreProcess

class GA():
    def __init__(self, coords, runs):
        self.runs = runs
        self.coords = coords
        self.N = len(self.coords)
        self.genes = [i for i in range(self.N)]
        self.chrom = 300
        self.pop = [random.sample(self.genes, self.N) for i in range(self.chrom)]

    def fitness(self, chromosome):
        ''' Calculate the total length (fitness) of a path. '''
        fitness = 0
        xs = [self.coords[chromosome[i%self.N]][0] for i in range(self.N+1)]
        ys = [self.coords[chromosome[i%self.N]][1] for i in range(self.N+1)]

        for k in range(self.N-1):
            fitness += math.sqrt((xs[k]-xs[k+1])**2 + (ys[k]-ys[k+1])**2)
        return fitness

    def selection(self, factor, p=[1,0]):
        """ Selection: stohastic universal sampling. """
        pop_sum = []
        self.new_pop = []
        total_fitness = sum([self.fitness(x) for x in self.pop])

        for x in self.pop:
            prob1 = (p[0]*(total_fitness - self.fitness(x))+p[1])
            prob2 = (p[0]*(total_fitness*(len(self.pop)-1))+p[1])
            prob = prob1/prob2
            pop_sum.append([x, prob])

        pop_sum.sort(key=lambda x:x[1])
        for i in range(1, len(pop_sum)):
            pop_sum[i][1] += pop_sum[i-1][1]

        r = random.random()
        for i in range(factor):
            sel_chrom = [x for x in pop_sum if x[1] >= (r+i/factor)%1][0]
            self.new_pop.append(sel_chrom[0])

    def crossover(self, parent1, parent2):
        ''' Crossover: select 2 sections from 2 chromosomes and swap them. '''
        cp1, cp2 = random.sample(range(self.N), 2)
        if (cp1 > cp2): cp1,cp2 = cp2,cp1

        child1 = copy.copy(parent1)
        child2 = copy.copy(parent2)
        j1 = cp1
        j2 = cp2

        for i in range(cp1, cp2):
            while parent2[j1] not in parent1[cp1:cp2]:
                j1 = (j1+1)%self.N
            child1[i] = parent2[j1]
            j1 = (j1+1)%self.N

            while parent1[j2] not in parent2[cp1:cp2]:
                j2 = (j2+1)%self.N
            child2[i] = parent1[j2]
            j2 = (j2+1)%self.N

        return child1, child2

    def mutation(self, chromosome):
        ''' Mutation: select two genes in a chromosome and swap them. '''
        mutated = copy.copy(chromosome)
        gene1, gene2 = random.sample(range(self.N), 2)
        mutated[gene1] = chromosome[gene2]
        mutated[gene2] = chromosome[gene1]
        return mutated

    def createOffspring(self, parents, p=0.1):
        ''' Applying crossover and mutation on parents. '''
        self.offspring = []

        for i in range(len(parents)):
            p1, p2 = random.sample(parents, 2)
            c1, c2 = self.crossover(p1, p2)
            self.offspring.append(c1)
            self.offspring.append(c2)

        for x in parents:
            if random.random() <= p:
                c = self.mutation(x)
                self.offspring.append(c)

    def elitismReplacement(self, population, n_elite):
        ''' Fill up population to a certain number. '''
        population.sort(key=lambda x: self.fitness(x))
        new_pop = population[:n_elite]
        self.offspring.sort(key=lambda x: self.fitness(x))
        new_pop.extend(self.offspring[:(len(self.pop) - n_elite)])
        return new_pop

    def genetic(self, plotPath=False):
        ''' Run Genetic Algorithm 'runs' times. '''
        for i in range(self.runs):
            self.selection(150)
            self.createOffspring(self.new_pop)
            self.pop = self.elitismReplacement(self.pop, 100)
            if (i+1)%50 == 0:
                print('------ run {} complete!'.format(i+1))

        best_path = min(self.pop, key=lambda x: self.fitness(x))
        # end path where it started
        best_path.append(best_path[0])

        if plotPath == True:
            dataPreProcess().plotPath(self.coords, best_path, self.N)

        return best_path, self.fitness(best_path)
