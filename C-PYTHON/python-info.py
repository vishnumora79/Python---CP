
import csv

mydict = {}
try:
 with open("python-info1.csv","r") as file:
     csv_read = csv.reader(file)
     
     next(csv_read)
     for row in csv_read:
      print(row)
      name,phone_number = row

      mydict[name] = phone_number

 print(mydict)
    

 while True:
  user_input = input("User input:")

  if user_input == 'C':
   name,phone = input(),int(input())
   mydict[name] = phone

  if user_input == "R":
    name = input()
    try:
     phone_number = mydict[name]
     print(f"Phone number for {name}:{phone_number}")
     
    except Exception as e:
        print("Name Not Found",e)
    
  if user_input == 'E':
    with open("python-info1.csv","r") as source_file:
        with open("python-copy-info1.csv","w",newline = '') as dest_file:
            csv_reader = csv.reader(source_file)
            csv_writer = csv.writer(dest_file)
            
            for l in csv_reader:
             csv_writer.writerow(l)
        print("New file created successfully")
    break     

except Exception as e:
       print("An Error Occurred",e)
