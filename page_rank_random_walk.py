import networkx as nx
import operator
import matplotlib.pyplot as py
import random
from networkx.algorithms.link_analysis.pagerank_alg import pagerank

G = nx.gnp_random_graph(10, 0.5, directed=True)
nx.draw(G, with_labels=True)
py.show()

rank = {}
x = random.choice([i for i in range(G.number_of_nodes())])

for i in range(G.number_of_nodes()):
    rank[i] = 0
rank[x] = rank[x]+1

i = 0
while(i < 10000000):
    n_neighbors = list(G.neighbors(x))
    if(len(n_neighbors) == 0):  # it is a sink
        x = random.choice([i for i in range(G.number_of_nodes())])
        rank[x] = rank[x]+1
    else:
        x = random.choice(n_neighbors)
        rank[x] = rank[x]+1
    i += 1

p = nx.pagerank(G)

print(sorted(p.items(), key=operator.itemgetter(1))) #1 for values and 0 for keys
print(sorted(rank.items(), key=operator.itemgetter(1)))
