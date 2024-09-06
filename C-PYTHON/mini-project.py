import csv

mydict = {}

try:
    file = open(r"E:\Python-py\C-PYTHON\mini-project-excel-data.csv","r")
    lines = file.readlines()

    for line in lines:
        l = line.split(",")
        print(l)

        roll, name, subject, grade = l

        mydict[roll] = [name,subject,grade]
    print(mydict)
    # file.close()
    while True:
        user = input("Enter command:")     

        if(user == 'C'):
            roll, name, subject, grade = int(input()), input(), input(), input()
            mydict[roll] = [name, subject,grade]

        elif(user == 'R'):
            roll_input = int(input())
            if roll_input in mydict.keys():
                roll_grade = mydict[roll][2]
                print("Grade of student with roll number %d is %s" %(roll_input,roll_grade))
            else:
                raise Exception("Name not found")
            
        # csv_file = "output.csv" 

        elif(user == 'E'):
            with open(r"E:\Python-py\C-PYTHON\mini-project-excel-data.csv", "a", newline = '') as file:
                csv_writer = csv.writer(file)

                csv_writer.writerow(mydict[0].keys()) 

                for data in mydict:
                     csv_writer.writerow(data.values())
                
            with open(r"E:\Python-py\C-PYTHON\mini-project-excel-data.csv", 'r') as file2:
             print(file2.read())
              

except Exception as e:
    print("Something whent wrong",e)        
