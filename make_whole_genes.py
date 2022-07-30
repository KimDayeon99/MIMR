#!/usr/bin/python
import sys

#set input file
intergest_path = "interest.genes.txt"
STRING_path = "/home/dayeon20/labProject/RWR-main/DATA/STRING_PPI_score.input"
#set output file
result_path="whole_genelist.txt"


tmp_dit = {}

with open(STRING_path,'r') as f_string, open(intergest_path,'r') as f_target, open(result_path,'w') as fw:
    for line in f_string:
        tmp = line.strip().split("\t")
        tmp_dit[tmp[0]]=1
        tmp_dit[tmp[1]]=1
    for line in f_target:
        tmp = line.strip()
        tmp_dit[tmp]=1
    keys = list(tmp_dit.keys())
    keys.sort()
    for key in keys:
        fw.write(key+"\n")
