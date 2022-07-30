#!/usr/bin/python
import sys

#set input file
DEmiRNA_path = sys.argv[1]
total_target_file = "/home/dayeon20/labProject/RWR-main/DATA/total.4DB.target.txt"
#set output file
result_path="./DEmiRNA.target.txt"

#load DEmiRNA data(input)
miRNAlist=[]
with open(DEmiRNA_path) as f:
    for element in f.read().splitlines():
        miRNAlist.append(element)

#write result
target_arr=[]
with open(total_target_file,'r') as fr,open(result_path,'w') as fw:
    for line in fr:
        tmp = line.strip().split("\t")
        miRNA = tmp[0]
        target = tmp[1]
        if miRNA in miRNAlist:
            if target not in target_arr:
                target_arr.append(target)
                fw.write(target+"\n")
