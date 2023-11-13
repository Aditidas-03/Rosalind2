from Bio import Phylo
from io import StringIO

with open('rosalind_nwck.txt') as file:
    data = file.read().strip().split('\n\n')#separating the different tree representations and their node pairs.

distance = []

for i in data:
    i = i.strip()
    start, end = i.split('\n')[1].split()#extracting the start and end nodes by splitting the data
    tree = Phylo.parse(StringIO(i), "newick") 

    for j in tree:
        if j.find_any(start) and j.find_any(end):#check if the start and end nodes are present in the current tree.
            path = j.trace(start, end)#if yes traces the path
            if path and path[0].name == start:#adjusts the path to remove the start node (if it's the initial node in the path)
                del path[0]
            distance.append(str(len(path)))#calculates distance

print(' '.join(distance))

