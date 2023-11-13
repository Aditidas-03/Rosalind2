
import sys
from Bio import Phylo
import io

f=open('rosalind_nkew.txt','r')
pairs=[i.split('\n') for i in f.read().strip().split('\n\n')]#splitting and creating a list

for i, line in pairs:
    x,y=line.split()#splitting into x,y
    tree=Phylo.read(io.StringIO(i),'newick')#parses the tree using newick
    print(round(tree.distance(x, y)), end=' ')#calculating and rounding the result

sys.stdout.write('\n')