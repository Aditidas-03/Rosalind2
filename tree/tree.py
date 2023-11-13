import networkx as nx

edges = []
with open('rosalind_tree.txt', 'r') as file:
        n = int(file.readline())  # no of nodes
        for line in file:
          edge = tuple(map(int, line.split()))
          edges.append(edge)


G=nx.Graph(edges)
max_edges=n-1
n_edges=G.number_of_edges()

min_edges= max_edges-n_edges
print(min_edges)
