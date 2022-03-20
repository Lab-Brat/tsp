import time, copy
from Data import dataPreProcess
from GA_TSP import GA
from SA_TSP import SA

coords = dataPreProcess().getLocs()

start = time.time()
GA = GA(coords, 200)
path_ga, path_fit_ga = GA.genetic()
end = time.time()
print("GA Total Distance: {0:.2f}, Time: {1:.2f}s".format(\
                                  path_fit_ga, end-start))

start = time.time()
SA_TSP = SA(coords)
path_sa, path_fit_sa = SA_TSP.sim_anneal()
end = time.time()
print("SA Total Distance: {0:.2f}, Time: {1:.2f}s".format(\
                                  path_fit_sa, end-start))

dataPreProcess().plot2Path(coords, path_ga, path_sa, len(coords))
