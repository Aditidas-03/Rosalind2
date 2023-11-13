from Bio import SeqIO
dna = list (SeqIO.parse("rosalind_splc.txt","fasta"))

dna_s = dna[0].seq
introns = [str(record.seq) for record in dna[1:]]
#remove introns
for intron in introns:
    dna_s=dna_s.replace(intron, '')
#converting into protein
mRNA = dna_s.transcribe()
protein = mRNA.translate()
print(protein)



