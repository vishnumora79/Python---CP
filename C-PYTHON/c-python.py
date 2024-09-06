import csv

mydict = {}

try:
    file = open(r"E:\Python-py\C-PYTHON\python-info1.csv","r")
    lines = file.readlines()
    for line in lines:
        l = line.split(",")
        print(l)
        name,phone_number = l
        mydict[name] = phone_number

    print(mydict)

    while True:
        user_input = input("User Input:")

        if user_input == "C":
           name,phone = input(),int(input())
           mydict[name] = phone

        elif user_input == 'R':
            name = input()
            if name in mydict.keys():
                phone_number = mydict[name]
                print(f"Phone number for {name}:{phone_number}")
            else:
                raise Exception("Name not found")

        elif user_input == 'E':
            with open("new_file.csv","w",newline = '') as file1:
                 writer = csv.writer(file1)
                 writer.writerow(['Name','Phone Number'])

            for name,phone_number in mydict.items():
                writer.writerow([name,phone_number])
                
            break
        
    with open("new_file.csv","r") as file2:
         print(file2.read())   
except Exception as e:
      print("Error Occurred",e)
    
