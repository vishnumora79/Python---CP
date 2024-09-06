#class Human:
   # def __init__(self):
    #    self.eyes = 2
     #   self.nose = 1
    #def eat(self):
      #  print("I can eat")
    #def work(self):
     #   print("I can work")

#class Male(Human):
  #  def flirt(self):
   #     print("I can flirt") 
    #def work(self):  #Overriding the method
     #   super().work()   #If you want to implement the super class methods also
           # super class used to access attributes and methods of parent class
      #  print("I can code")    


#male_1 = Male()  # Object creation

#male_1.flirt()   # Method of male class

#male_1.work()    # Implements both parent and child class method.

#print(male_1.eyes)  


class Human:
    def __init__(self,can_speak = True):
        self.eyes = 2
        self.nose = 1
        self.can_speak = can_speak
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self,name,can_speak):
        super().__init__(can_speak)
        self.name = name
    def flirt(self):
        print("I can flirt")

male_1 = Male("samson",True)     

male_1.eat()
print(male_1.eyes)
print(male_1.name)
print('Yes, he can speak' if male_1.can_speak else 'No, Unfortunatly he cannot')




