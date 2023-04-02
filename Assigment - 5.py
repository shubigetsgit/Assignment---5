#Challenge 1
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def sqSum(self):
         print((self.x**2)+(self.y**2)+(self.z**2))
    
numbers = Point(1,3,5)
numbers.sqSum()

#Challenge 2
class Calculator:
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print((self.num1)+ (self.num2))
    def subtract(self):
        print((self.num2)- (self.num1))
    def multiply(self):
        print((self.num1 )* (self.num2))
    def divide(self):
        print((self.num2)/ (self.num1))

obj = Calculator(10, 94)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()

#Challenge3
class Student:
    __name = ""
    __rollNumber  = ""
    
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
        
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    def getRollNumber(self):
        return self.__rollNumber
    
student = Student()
student.setName("John")
student.setRollNumber("12345")
print(student.getName())     
print(student.getRollNumber()) 
    




#Challenge4
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = Account("Ashish", 5000)
print(account1.title)  
print(account1.balance)  

account2 = SavingsAccount("Ashish", 5000, 5)
print(account2.title) 
print(account2.balance)
print(account2.interestRate)  



#Challeng5
class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount
        

    def deposit(self,amount):
        self.balance += amount

    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        print (((self.interestRate) * (self.balance))/100)
 
    
demo1 = Account("Ashish", 2000) 
demo1.deposit(500)
print(demo1.getBalance())

demo1 = Account("Ashish", 2000) 
demo1.withdrawal(500)
print(demo1.getBalance())

demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.interestAmount()