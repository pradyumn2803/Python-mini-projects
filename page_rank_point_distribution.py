from hashlib import new
import networkx as nx
import matplotlib.pyplot as py
import random
from networkx.algorithms import operators

from networkx.algorithms.isomorphism.tree_isomorphism import assign_levels


def add_edges():
    nodes = list(G.nodes())
    for t in range(len(nodes)):
        for s in range(len(nodes)):
            if t != s:
                r = random.random()
                if(r <= 0.5):
                    G.add_edge(s, t)
    return G


def assign_points(G):
    nodes = list(G.nodes())
    p = []
    for i in range(len(nodes)):
        p.append(100)
    return p


def distribute(points):
    new_points = []
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        new_points.append(0)
    for n in nodes:
        out = list(G.out_edges(n))
        if(len(out) == 0):
            new_points[n] = new_points[n]+points[n]
        else:
            share = points[n]/len(out)
            for (src, tgt) in out:
                new_points[tgt] += share
    return new_points


def keep_distribute(G, points):
    i=0
    while i<1000000:
        new_points = distribute(points)
        points = new_points
        # print(new_points)
        i+=1
        # i = input('press 0 to quit and any key to continue :')
        # if(i == '0'):
        #     break
    return points

def rank_by_points(points):
    d = {}
    for i in range(len(points)):
        d[i] = points[i]
    print('Final points are\n')
    print(sorted(d.items(), key=lambda f: f[1]))
    # sorted(d.items(),key = operators.itemsetter(1))
    


G = nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G = add_edges()

# nx.draw(G,with_labels=True)
# py.show()

points = assign_points(G)

final_points = keep_distribute(G, points)

rank_by_points(final_points)
result = nx.pagerank(G)
print()
print(sorted(result.items(), key=lambda f: f[1]))
