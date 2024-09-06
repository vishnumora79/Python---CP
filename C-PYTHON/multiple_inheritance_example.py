class Person:
    def __init__(self,name,can_dance = False):
        self.name = name
        self.can_dance = can_dance
        print("Calling init function of Person class")
    def learn_pratice(self):
        return f"{self.name} learn new things and practice them for 12 hours everyday"

class Male:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Calling init function of Male class")
    def future_plans(self):
       return "Reaching the  level of expertize"
    def marriage(self):
        return f"{self.name} looking to get marrid at the age of {self.age}"
    
class Boy(Person,Male):
    def __init__(self,name,can_dance,age,no_of_friends):
        Person.__init__(self,name,can_dance)
        Male.__init__(self,name,age)
        self.no_of_friends = no_of_friends
    def alone(self):
        return f"{self.name} is staying alone will help in sometimes but not everytime. He is lacking of {self.no_of_friends} good friends"        

        
buddy = Boy('bilder',True,27,4)

print(buddy.learn_pratice())
print(buddy.alone())
print(buddy.future_plans())
print(buddy.marriage())

