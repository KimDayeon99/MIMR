#!/usr/bin/python
import sys

#set input file
gene_path = sys.argv[1]
target_path = "DEmiRNA.target.txt"
#set output file
result_path = "interest.genes.txt"


DEmiRNA_target = []
core_target = []
with open(target_path,'r') as f_target, open(gene_path,'r') as f_gene, open(result_path,'w') as fw:
    for line in f_target:
        tmp = line.strip()
        fw.write(tmp+"\n")
        DEmiRNA_target.append(tmp)
    for line in f_gene:
        tmp = line.strip()
        if tmp in DEmiRNA_target:
            core_target.append(tmp)
        else:
            fw.write(tmp+"\n")
