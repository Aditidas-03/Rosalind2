from Bio import SeqIO
import networkx as nx
dna=list(SeqIO.parse("rosalind_grph.txt", "fasta"))
'''O=nx.Graph()
#adding nodes from seq
for seq in dna:
    O.add_node(str(seq.id))
 
#finding the overlap in tail of s and head of t
k=3
for s in dna:
    for t in dna:
         if s.id != t.id and str(s.seq)[-k:] == str(t.seq)[:k]:
             O.add_edge(str(s.id), str(t.id))

a_list=list(O.edges())
for edge in a_list:
    print(f"{edge[0]} {edge[1]}")
    
    #this doesn't work.why :")
'''

k = 3
a_dic= {}


for i in range(len(dna)):
    for j in range(len(dna)):
        if i!= j:
            s = str(dna[i].seq)
            t = str(dna[j].seq)
            if s[-k:] == t[:k]:
                if dna[i].id not in a_dic:
                    a_dic[dna[i].id] = []
                a_dic[dna[i].id].append(dna[j].id)

for key, values in a_dic.items():
    for value in values:
        print(f"{key} {value}")



