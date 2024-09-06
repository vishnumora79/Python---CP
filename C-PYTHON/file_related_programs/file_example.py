# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:18:03 2023

@author: vishn
"""

fo = open("data.txt","w")

txt = ['Hello!', 'Good Morning', 'How are you']

fo.writelines(txt)

fo.close()


fo = open("data.txt",'w')

fo.write("We in learning phase \n")

fo.close()

fo = open("data.txt",'a')

fo.write("Somthing is learning today!")

fo.close()

fo = open("data.txt",'r')

f1 = fo.read(15)

print(f1)
print(len(f1))
fo.close()

fo = open("data.txt",'r')

print(fo.readline())

fo.close()

fo = open("data.txt",'r')

print(type(fo.readlines()))

fo.close()

with open("data.txt",'r') as file:
     for line in file:
         print(line)
         
# =============================================================================
# file attributes         
# =============================================================================
fo = open("data.txt",'w')
print(fo.name)
print(fo.closed)
print(fo.mode)

#import os

#file_path = os.path.abspath("data.txt")

#print(file_path)
