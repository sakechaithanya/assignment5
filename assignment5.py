#1challenge
class var:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def  sqsum(self):
       self.x=self.x*self.x
       self.y=self.y*self.y
       self.z=self.z*self.z
       return self.x+ self.y+ self.z
        
result=var(1,3,5)   
print(result.sqsum())

#2challenge
class calulator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def subtract(self):
        if self. num1>self.num2:
           return  self.num1-self.num2
        else:
             return self.num2-self.num1
    def multiply(self):
        return  self.num1*self.num2
    def div(self):
        if self. num1>self.num2:
           return  self.num1/self.num2
        else:
           return  self.num2/self.num1
result=calulator(10,94)  
print(result.add())
print(result.subtract())
print(result.multiply())
print(result.div())      

#3challenge
class student:
    def setName(self,__name,key):
        if key=="chay":
         self.__name=__name
        else:
           print("incorrect key")
        
    def getName(self):
        if self.__name=="sake:
         print(" yes its crt name",self.__name)
        else:
            print("incorrect name!")
    def setRollNumber(self,__rollnumber,key):
        if key=="chey":
         self.__rollnumber=__rollnumber
        else:
           print("incorrect key")
    def getRollNumber(self):
        if self.__rollnumber==575:
            print("yes its crt roll number",self.__rollnumber)
        else:
            print("incorrect rollnumber")    
result=student()  
result.setName("sake","chay")     
result.setRollNumber(575,"chey")
result.getName()
result.getRollNumber()

#4challenge
class account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance

class Savaccount(account):
    def __init__(self, title,balance,interest):
        super(Savaccount,self).__init__(title, balance)
        self.interest=interest
        self.interest= self.balance*self.interest/100
        print(self.interest)
result=Savaccount("sake",5000,5) 

#5challenge
class account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
    def deposit(self, d):
        self.balance = self.balance + d
        print(self.balance)
    def Withdrawal(self , w): 
        if(self.balance < w):
          print("impossible operation! Insufficient balance !")
        else:
           self.balance = self.balance - w
           print(self.balance)
    def getBalance(self):
       print(self.balance)
       

class Savaccount(account):
    def __init__(self, title,balance,interest):
        super(Savaccount,self).__init__(title, balance)
        self.interest=interest
        self.interest= self.balance*self.interest/100
        print(self.interest)
result=Savaccount("sake",5000,5) 
result.getBalance()
result.deposit(100)
result.Withdrawal(10)




        
     




        
     
