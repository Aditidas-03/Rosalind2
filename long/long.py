from Bio import SeqIO

sss=[]

for record in SeqIO.parse('rosalind_long.txt', "fasta"):
        sss.append(str(record.seq))
        length=len(str(record.seq))

length = len(sss[0])
for i in range(length):
    for s1 in sss:
        for s2 in sss:
            if s1 != s2:#making sure both are not same
                for j in range(len(s1)):
                    if s1[:j] == s2[-j:]and j >= int(length//2)-1:#checking overlap and its length is more than half
                        sss.append(s2+s1[j:])
                        if s1 in sss:
                            sss.remove(s1)#removing if its already present
                        if s2 in sss:
                            sss.remove(s2)#same
print(sss)
