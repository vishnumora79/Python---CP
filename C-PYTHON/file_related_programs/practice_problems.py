# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:33:32 2023

@author: vishn
"""

# Example - 1  -------------  creating a file where input given by user will be stored in that created file.
def file1():
    f1 = open(r"E:\Python-py\C-PYTHON\file_related_programs\about.txt",'w')
    text = input("Enter something about you:")
    f1.write(text)
    f1.close()

file1()


# Example - 2 ----------- creating a file where first name, middle name, lastname  of the user will be stored in file line by line
def file2():
    f2 = open(r"E:\Python-py\C-PYTHON\file_related_programs\Myname.txt","w")
    fn = input("Enter first name:")
    mn = input("Enter Middle name:")
    ln = input("Enter last name:")
    nextline = "\n"
    f2.write(fn)
    f2.write(nextline)
    f2.write(mn)
    f2.write(nextline)
    f2.write(ln)
    f2.write(nextline)
    f2.close()
    
file2()    

# Example - 3 ----------- creating a new file by merging two different files
def file3():
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\about.txt",'r') as file1:
         data1 = file1.read()
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\Myname.txt") as file2:
         data2 = file2.read()
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\mergefile.txt","w") as file3:
        file3.write(data1)
        file3.write("\n")
        file3.write(data2)
        
file3()       

# Example - 4 ------- To count the occurances of a word in a file
def file4():
    count = 0
    word_search = input("Enter word to search occrances:")
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\mergefile.txt",'r') as file:
         for line in file:
             words = line.split()
             for word in words:
                 if(word == word_search):
                     count += 1
    print(f"{word_search} word occurs {count} time in file mergefile.txt")

file4() 

# Example - 5 ----- Replace all blank spaces with " * "
def file5():
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\mergefile.txt",'r') as file:
         data = file.read()
         data = data.replace(" ","_")
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\blank_space.txt",'w') as file1:
         file1.write(data)
         
file5()         

# Example - 6 ----- writing a list to a file
def file6():
    list1 = ['Ajay','Amit','Anmol','Bajrang']
    with open(r"E:\Python-py\C-PYTHON\file_related_programs\list.txt",'w') as file:
        for l in list1:
            file.write(l + "\n")
            
file6()            
        
 
# Example - 7 -------- finding the size of a file

import os

file_path = r"E:\Python-py\C-PYTHON\file_related_programs\about.txt"

size = os.path.getsize(file_path)

print(f"The size of {file_path} is {size} bytes.")
    
# Example - 8 ----- To check if a file is exists or not

import os

file_path = "E:\Python-py\C-PYTHON\file_related_programs\about1.txt"

flag = os.path.isfile(file_path)

if flag:
    print(f"The given file {file_path} exists.")
else:
    print(f"The given file doesn't exists")    
    
    
# Example - 9 ---- To store all file lines in a list

list1 = []

with open(r"E:\Python-py\C-PYTHON\file_related_programs\check.txt",'r') as file:
     list1 = file.readlines()
     
with open(r"E:\Python-py\C-PYTHON\file_related_programs\check.txt",'w') as file:
     for number, line in enumerate(list1):
         if number not in [4,7]:
             file.write(line)
             
             
# Example - 10 ----- simple example

with open(r"E:\Python-py\C-PYTHON\file_related_programs\check.txt",'r') as file:
     line_numbers = [4,7]
     lines = []

     for i, line in enumerate(file):
         if i in line_numbers:
            lines.append(line.strip())
         elif i > 7:
            break
print(lines)             

    
    
    