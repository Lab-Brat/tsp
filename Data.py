import random, re
import matplotlib.pyplot as plt

p = re.compile(r'^(\d{1,3}) (\d{1,3})$')
with open("locations.txt") as txt:
    coords = [[int(i) for i in p.search(l).groups()] for l in txt.readlines()]


res1 = [5,10,15,20,25,30,35,40]     # only visit 3 of these
res2 = [2,4,6,8,10,20,22,32,33,35]  # only visit 5 of these

class dataPreProcess():
    def __init__(self):
        self.data = coords
        self.ran_seq = random.sample(range(1,len(self.data)+1), len(self.data))
        self.res1 = res1
        self.res2 = res2

    def getInds(self):
        '''Select locations to visit and output their indices'''
        # visit at least 3 locations from res1, and 5 from res2
        res1_sel = random.sample(self.res1, 3)
        res2_sel = random.sample(self.res2, 5)

        # select unique locations
        res_set = set(res1).union(set(res2))
        res_sel_set = set(res1_sel).union(set(res2_sel))

        # remove all restricted locations, then add the selected ones
        fin_seq = [i for i in self.ran_seq if i not in res_set]
        fin_seq.extend(res_sel_set)
        return fin_seq

    def getLocs(self):
        ''' Output actual locations from data using selected locations '''
        # sort indices, then use them to find locations in data
        coords_indx_sort = sorted(self.getInds())
        coords_list = [self.data[i-1] for i in coords_indx_sort]

        # start and finish at the depot coordinate
        depot = [0,0]
        coords_list.insert(0, depot)
        coords_list.append(depot)

        return coords_list

    def plotPath(self, coords, path, N):
        xs = [coords[path[i]][0] for i in range(N+1)]
        ys = [coords[path[i]][1] for i in range(N+1)]
        plt.plot(xs, ys, 'ob-')
        plt.show()

    def plot2Path(self, coords, path1, path2, N):
        xs1 = [coords[path1[i]][0] for i in range(N+1)]
        ys1 = [coords[path1[i]][1] for i in range(N+1)]
        xs2 = [coords[path2[i]][0] for i in range(N+1)]
        ys2 = [coords[path2[i]][1] for i in range(N+1)]

        fig, axs = plt.subplots(1,2, figsize=(9.7, 5))
        fig.suptitle('Shortest paths by GA(left) and SA(right)')
        axs[0].plot(xs1, ys1, 'ob-')
        axs[1].plot(xs2, ys2, 'om-')
        plt.show()
