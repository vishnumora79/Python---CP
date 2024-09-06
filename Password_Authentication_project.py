import getpass
database = {'vishnu':'vishnuyt@81' , 'anjani' : 'anju@79'}
username = input("enter your username:")
password = getpass.getpass("enter your password:")
for i in database.keys():
    if (username != i):
       print("Username is incorrect!")
       
    else:   
       while password != database.get(i):
             print("Incorrect Password🚫") 
             password = getpass.getpass("enter password again:") 
             continue  
print("Verified!✅")       
# import getpass
# database = {'vishnu':'vardhan' , 'anjani':'mora'}
# username = input("Enter username:")
# password = getpass.getpass("Enter Password:")
# while True:
#     if username == database.keys():
#         if password == database[username]:
#            Print("Verification -- Successful!")
#            break
#         else:
#             print("Incorrect password!")
#             password = getpass.getpass("Enter password again!") 
         