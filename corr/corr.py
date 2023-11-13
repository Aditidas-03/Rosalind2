from Bio import SeqIO

def hamm_distance(s1, s2):
    return sum([1 if s1[i]!=s2[i] else 0 for i in range(len(s1))])#creating a function to check for the hamm dist
def corr(reads):#creating the proof reading function
    correction = []
    corr_reads, incorr_reads = [], []
    nuc_com={"A": "T", "T": "A", "C": "G", "G": "C"}#a dict for the
    for read in reads:
        reverse_r = "".join([nuc_com[i] for i in read[::-1]])
        if reads.count(read) + reads.count(reverse_r) >= 2:#checks if the read count of it and complement is more than 2
            corr_reads.append(read)
        else:
            incorr_reads.append(read)

    for ir in incorr_reads:
        for cr in corr_reads:
            reverse_cr = "".join([nuc_com[i] for i in cr[::-1]])#compares it to the correct reads and their reverse complements using the Hamming distance function
            if hamm_distance(ir, cr) == 1:
                correction.append((ir, cr))
                break
            if hamm_distance(ir, reverse_cr) == 1:
                correction.append((ir, reverse_cr))
                break

    return correction


seq_name, seq = [], []
    
for seq_record in SeqIO.parse('rosalind_corr.txt','fasta'):
    seq_name.append(str(seq_record.name))
    seq.append(str(seq_record.seq))

correction = corr(seq)
for ir, cr in correction:
    print("{}->{}".format(ir, cr))











