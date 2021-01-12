#!/usr/bin/env python3
#This code deletes all .py files with '#Virus' line
import glob,re,os,sys
def search():
    files=glob.glob('*.py')
    self_name = os.path.basename(__file__)
    if self_name in files:
        files.remove(self_name)
    return files
def destroy(files):
    for virus in files:
        Infected = False
        with open(virus, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if re.search('#Virus', line):
                    Infected = True
                    break
        if Infected:
            os.remove(virus)
            print("deleted {}".format(virus))
contents=search()
destroy(contents)
