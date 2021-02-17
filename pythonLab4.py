
#  -----------------------------------1--------------------------------

class Vehicle:
    color ='White'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
c1 =Car('x' ,'50','1000')
print(c1.color)


# --------------------------2-----------

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        full= self.capacity*100 
        return(full+full*0.1)

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())





# --------------------------3-----------


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(School_bus,Vehicle))





# # -------------------------------4----------------------------
class Rectangle :
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return(self.width*self.length)

R1 =Rectangle(5,10)

print(R1.area())


# -------------------------------5----------------------------

class Str :
    def getString(self):
        self.x= input("enter string :")

    def printString(self):
        print(self.x)
        

s =Str()

s.getString()
s.printString()




# ---------------------------6-----------------------------

class Person:
    def getGender(self):
        return('Person')
class Male(Person):
    def getGender(self):
        return('male')    
class Female(Person):
     def getGender(self):
        return('female')   
m1 =Male()
print(m1.getGender())



#------------------------------7----------------------

class Parentheses:
    def __init__(self,myStr):
        self.myStr=myStr

    def checkValidity(self):
        dict1= {')':'(' , ']':'[' ,'}':'{'}
        stack=[]
        valid=True
        length=len(self.myStr)
        if length %2 !=0 :
            return False
        for i in range(length):
            if self.myStr[i] in dict1.values() :
                stack.append(self.myStr[i])
            elif self.myStr[i] in dict1.keys() :
                if(stack[-1] == dict1[self.myStr[i]]):
                    stack.pop()
                    continue
                else:
                    return False
            else:
                return False                    
        return(valid)


p1=  Parentheses("(){()}[]")

print(p1.checkValidity())
    