from Bio import SeqIO

records = SeqIO.parse("covid19.fasta", "fasta")
count = SeqIO.write(records, "covid19.fastq", "fastq")
print("Converted %i records" % count)

